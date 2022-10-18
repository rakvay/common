#!/usr/bin/env python3
"""
Simple Click example
"""
import click

@click.command()
@click.option('--greeting', default='Hiya', help='How do youwant to greet?')
@click.option('--name', default='Tammy', help='Who do youwant to greet?')
def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    greet()
