output "resource_group_name" {
  description = "Name of the Resource Group"
  value       = data.azurerm_resource_group.main.name
}

output "acr_login_server" {
  description = "Azure Container Registry login server URL"
  value       = azurerm_container_registry.acr.login_server
}

output "acr_name" {
  description = "Azure Container Registry name"
  value       = azurerm_container_registry.acr.name
}

output "container_app_url" {
  description = "Public URL of the Policy API"
  value       = "https://${azurerm_container_app.policy_api.ingress[0].fqdn}"
}

output "application_insights_key" {
  description = "Application Insights instrumentation key"
  value       = azurerm_application_insights.main.instrumentation_key
  sensitive   = true
}

output "log_analytics_workspace_id" {
  description = "Log Analytics Workspace ID"
  value       = azurerm_log_analytics_workspace.main.id
}
