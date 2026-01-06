# Azure Landing Zone – Hub & Spoke Architecture (Non-Prod)

## Overview
This project demonstrates a production-style **Azure Landing Zone (ALZ)** network foundation using a **Hub-and-Spoke architecture**.  
It focuses on secure traffic flow, centralized egress, governance, and cost-aware design aligned with enterprise cloud platform engineering standards.

The implementation mirrors patterns used in regulated and large-scale environments such as utilities, finance, and healthcare.

---

## Architecture Summary
- **Hub VNet**
  - Centralized connectivity
  - Azure Firewall for outbound traffic inspection
- **Spoke VNet**
  - Workload subnet hosting Linux VM
  - No direct internet exposure
- **User Defined Routes (UDR)**
  - Default route (`0.0.0.0/0`) forces traffic through the hub firewall
- **VNet Peering**
  - Hub ↔ Spoke connectivity
- **Azure Policy**
  - Subscription-level security and compliance baseline
- **Cost Optimization**
  - Azure Spot VM
  - VM deallocated when not in use

---

## Key Azure Services Used
- Azure Virtual Networks (Hub & Spoke)
- Azure Firewall + Firewall Policy
- User Defined Routes (UDR)
- VNet Peering
- Azure Policy Assignments
- Azure Virtual Machines (Linux)
- Azure Monitor (route validation)

---

## Traffic Flow Design
1. Workload VM resides in **spoke workload subnet**
2. Subnet UDR overrides Azure default routing
3. All outbound traffic (`0.0.0.0/0`) is sent to:
   - **Next hop: Virtual Appliance**
   - **IP: Azure Firewall private IP**
4. Effective Routes confirm user-defined routing precedence

This ensures:
- Centralized inspection
- No direct internet breakout from spokes
- Predictable, auditable traffic paths

---

## Validation & Evidence
The following screenshots demonstrate correct platform behavior:

- Hub ↔ Spoke VNet Peering (Connected)
- User Defined Route forcing default traffic to firewall
- Effective Routes showing UDR override
- Azure Firewall Policy configuration
- VM deployed in spoke workload subnet
- Cost-optimized VM state (deallocated)

> Screenshots are provided in this repository to validate real Azure control-plane behavior.

---

## Cost Awareness
To minimize ongoing cost while preserving architectural integrity:
- Azure Spot VM is used
- VM is stopped/deallocated when not actively tested
- No public IPs assigned to workloads

---

## Why This Matters
This project reflects:
- Enterprise network segmentation
- Zero-trust traffic control principles
- Cloud governance fundamentals
- Real Azure troubleshooting and validation skills

It is designed to be **discussed live during interviews**, including trade-offs, design decisions, and operational considerations.

---

## Future Enhancements (Planned)
- Terraform IaC implementation
- Azure Bastion integration
- Azure Monitor + Log Analytics traffic logging
- Private DNS Zones
- CI/CD deployment of network components

---

## Author
Luis Antonio  
Cloud & Platform Engineering Focus
