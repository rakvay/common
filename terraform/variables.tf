variable "project_id" {
  description = "The project ID to host the cluster in"
  default     = "perfect-entry-310511"
}

variable "cluster_name_suffix" {
  description = "A suffix to append to the default cluster name"
  default     = ""
}

variable "region" {
  description = "The region to host the cluster in"
  default     =  "europe-west4"
}

variable "router_name" {
  description = "The name of the router"
  default     =  "artem-router"
}

variable "zones" {
  type        = list(string)
  description = "The zone to host the cluster in (required if is a zonal cluster)"
  default     = ["europe-west4-a", "europe-west4-b", "europe-west4-c"]
}

variable "network" {
  description = "The VPC network to host the cluster in"
  default     = "artem-net"
}

variable "subnetwork" {
  description = "The subnetwork to host the cluster in"
  default     = "artem-sub"
}

variable "ip_range_pods_name" {
  description = "The secondary ip range to use for pods"
  default     = "artem-private-pods"
}

variable "ip_range_services_name" {
  description = "The secondary ip range to use for pods"
  default     = "artem-private-services"
}

variable "compute_engine_service_account" {
  description = "Service account to associate to the nodes in the cluster"
}
