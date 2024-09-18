variable "digitalocean_token" {
  type        = string
  description = "DigitalOcean API token"
  sensitive   = true # Sensitive so that it won't be seen in the logs
}

variable "ssh_key_name" {
  description = "SSH key"
  type        = string
}

variable "ssh_public_key" {
  description = "The content of SSH public key"
  type        = string
}