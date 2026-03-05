variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-super-duper-forsakring"
}

variable "location" {
  description = "Azure region for all resources"
  type        = string
  default     = "swedencentral"
}

variable "project_name" {
  description = "Short project name used for resource naming"
  type        = string
  default     = "superduper"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "prod"
}
