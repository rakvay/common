terraform {
  required_version = "0.14.10"
}

locals {
  cluster_type = "node-pool"
}

module "vpc" {
  source       = "terraform-google-modules/network/google"
  version = "~> 3.0"
  project_id   = var.project_id
  network_name = var.network

  subnets = [
    {
      subnet_name   = var.subnetwork
      subnet_ip     = "10.0.0.0/24"
      subnet_region = var.region
    },
  ]

  secondary_ranges = {
    "${var.subnetwork}" = [
      {
        range_name    = var.ip_range_pods_name
        ip_cidr_range = "10.0.32.0/20"
      },
      {
        range_name    = var.ip_range_services_name
        ip_cidr_range = "10.0.64.0/24"
      },
    ]
  }
}

module "cloud_router" {
  source  = "terraform-google-modules/cloud-router/google"
  version = "~> 0.4"

  name    = var.router_name
  project = var.project_id
  region  = var.region
  network = var.network
}

module "address" {
  source  = "terraform-google-modules/address/google"
  version = "2.0.0"
  region  = var.region
  project_id  =  var.project_id
}

module "cloud-nat" {
  source     = "terraform-google-modules/cloud-nat/google"
  version    = "~> 1.2"
  router     = var.router_name
  project_id = var.project_id
  region     = var.region
  name       = "my-cloud-nat-${var.router_name}"

//  nat_ip_allocate_option = "MANUAL_ONLY"
//  nat_ips = module.address.self_links
}

module "gke" {
  source                 = "terraform-google-modules/kubernetes-engine/google//modules/private-cluster/"
//  version = "~> 3.0"
  project_id             = var.project_id
  name                   = "${local.cluster_type}-${var.cluster_name_suffix}-cluster"
  regional               = true
  region                 = var.region
  zones                  = var.zones
  network                = var.network
  subnetwork             = var.subnetwork
  ip_range_pods          = var.ip_range_pods_name
  ip_range_services      = var.ip_range_services_name
  create_service_account = false
  enable_private_endpoint = false
  enable_private_nodes    = true
  master_ipv4_cidr_block  = "10.5.5.0/28"
  
  node_pools = [
    {
      name               = "artem-node-pool"
      machine_type       = "n1-standard-2"
      min_count          = 1
      max_count          = 1
      disk_size_gb       = 30
      disk_type          = "pd-standard"
      image_type         = "COS"
      auto_repair        = true
      auto_upgrade       = true
      service_account    = var.compute_engine_service_account
      preemptible        = false
      initial_node_count = 1
    },
  ]
}
