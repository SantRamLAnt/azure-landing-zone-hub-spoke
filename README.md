# Azure Landing Zone – Hub and Spoke Portfolio

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://azure-landing-zone-hub-spoke.streamlit.app)

## 🚀 Live Demo

**[View Interactive Portfolio →](https://azure-landing-zone-hub-spoke.streamlit.app)**

---

## Overview

This repository documents a non-production **Azure Landing Zone** implementation using a **hub-and-spoke network topology**. The project demonstrates **governance, centralized networking, controlled egress routing, and policy-first security design**, aligned with enterprise Azure best practices.

The environment was intentionally designed to balance **technical depth, cost efficiency, and interview readiness**.

## What This Project Demonstrates (At a Glance)

- Enterprise Azure Landing Zone design
- Governance-first subscription and policy strategy
- Centralized egress control using UDRs
- Security decoupled via Azure Firewall Policy
- Runtime validation using Effective Routes
- Cost-aware architectural decision making

---

## Architecture Summary

### Topology

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MANAGEMENT GROUPS                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │   Root   │→ │ Platform │→ │ Landing Zones│→ │Workload(NonProd)│ │
│  └──────────┘  └──────────┘  └──────────────┘  └────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         NETWORK TOPOLOGY                            │
│                                                                     │
│   ┌─────────────────────┐          ┌─────────────────────┐         │
│   │     HUB VNET        │          │    SPOKE VNET       │         │
│   │   10.0.0.0/16       │◄────────►│   10.1.0.0/16       │         │
│   │                     │  Peering │                     │         │
│   │ ┌─────────────────┐ │          │ ┌─────────────────┐ │         │
│   │ │ Firewall Policy │ │          │ │  Workload VM    │ │         │
│   │ │    10.0.0.4     │ │◄─────────│ │   10.1.0.4      │ │         │
│   │ └─────────────────┘ │   UDR    │ └─────────────────┘ │         │
│   └─────────────────────┘          └─────────────────────┘         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### IP Design

| Component | CIDR Block |
|-----------|------------|
| Hub VNet | 10.0.0.0/16 |
| Spoke VNet | 10.1.0.0/16 |
| Workload Subnet | 10.1.0.0/24 |

---

## Governance & Management

### Management Groups

- Root
- Platform
- Landing Zones
- Workload (NonProd)

### Azure Policy

Required resource tags enforced at subscription scope:
- `Owner` - Accountability tracking
- `Environment` - Lifecycle stage (NonProd)
- `Application` - Workload identification

This ensures governance, cost attribution, and ownership tracking from resource creation.

---

## Networking

### Hub-and-Spoke Design

- VNet peering configured with forwarded traffic allowed
- No direct internet egress from spoke workloads

### User Defined Routes

| Route Name | Address Prefix | Next Hop Type | Next Hop Address |
|------------|---------------|---------------|------------------|
| default-to-hub | 0.0.0.0/0 | Virtual Appliance | 10.0.0.4 |

### Routing Validation

A test VM was deployed to create a NIC. Effective Routes were validated at the NIC level, confirming:
- ✅ Azure default internet route is **Invalid**
- ✅ User-defined route forwards traffic toward the hub

---

## Security (Policy-First Firewall Design)

An **Azure Firewall Policy** was created to demonstrate centralized, scalable security governance without deploying a full firewall instance.

### Firewall Policy Components

- Rule Collection Group: `rcg-nonprod-egress`
- Network Rule Collection: DNS / NTP egress
- Application Rule Collection: OS and package update endpoints (FQDN-based)

This reflects a **policy-first approach**, allowing security rules to be designed, reviewed, and versioned independently of enforcement infrastructure.

---

## Cost Management

Cost-aware decisions were intentionally applied:

| Decision | Savings |
|----------|---------|
| Azure Spot VM | Up to 90% vs on-demand |
| VM deallocated after validation | $0 compute when idle |
| No firewall runtime deployed | ~$900/month saved |
| No always-on compute resources | Variable cost only |

This approach enables architectural validation without unnecessary cloud spend.

---

## Validation Evidence

The following validations were performed:

- [x] Hub ↔ Spoke peering connectivity
- [x] UDR enforcement
- [x] Runtime route validation via **Effective Routes**
- [x] Governance enforcement via Azure Policy
- [x] Firewall Policy configuration
- [x] Cost optimization verification

---

## Screenshots

### VNet Peering
![VNet Peering](screenshots/networkingpeer.png)

### Effective Routes (UDR Validation)
![Effective Routes](screenshots/VMRoute.png)

### UDR Configuration
![UDR](screenshots/networkingudr.png)

### Azure Policy
![Azure Policy](screenshots/azurepolicyrequired.png)

### Firewall Policy
![Firewall Policy](screenshots/securityfirewall.png)

### Cost-Aware VM (Deallocated)
![VM Deallocated](screenshots/costvmdeallocated.png)

---

## Interview Walkthrough

During an interview, this project can be presented as:

1. **Governance first** (management groups + policy)
2. **Network segmentation** (hub-and-spoke)
3. **Traffic control** (UDRs)
4. **Security design** (firewall policy)
5. **Runtime validation** (effective routes proof)
6. **Cost optimization decisions**

---

## Technologies Demonstrated

- Azure Management Groups
- Azure Policy & RBAC
- Virtual Networks & Peering
- User Defined Routes (UDRs)
- Azure Firewall Policy
- Azure Spot VMs
- Resource Tagging Strategy

---

## About the Author

**Luis Antonio Santiago-Ramirez**

- 🏢 GIS Associate Technician at Eversource Energy
- 🎓 Pursuing M.Eng Computer Engineering at Dartmouth College
- ☁️ Azure Certified: AZ-500, AZ-400, AI-102, DP-203

This project was developed independently outside of work hours using personal resources. No Eversource data or systems were used.

---

## Connect

- [LinkedIn](https://www.linkedin.com/in/luisantoniosantiago-ramirez-70b418196)
- [GitHub](https://github.com/SantRamLAnt)
- 📧 lasrsecond@gmail.com
