# IAM Connector Simulator

A REST API simulating a business application target system 
for IAM connector integration — built to demonstrate 
enterprise identity lifecycle management concepts.

## What This Simulates
- Account aggregation (GET /users)
- User provisioning (POST /users)
- User deprovisioning (POST /users/<id>/disable)
- Health check endpoint (GET /health)

## Tech Stack
- Python / Flask
- AWS EC2 (Ubuntu)
- GitHub Actions (CI/CD)
- REST API / JSON

## Deployment
Automatically deployed to AWS EC2 via GitHub Actions 
on every push to main branch.

## IAM Concepts Demonstrated
- REST connector integration pattern
- Identity lifecycle (provision → active → disabled)
- Automated deployment pipeline
- Secure server access via SSH key authentication
- Network security via AWS security groups