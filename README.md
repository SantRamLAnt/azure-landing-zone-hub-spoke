# Azure Landing Zone – Hub and Spoke (Non-Production)

## Overview

This repository documents a non-production **Azure Landing Zone** implementation using a **hub-and-spoke network topology**.
The project demonstrates **governance, centralized networking, controlled egress routing, and policy-first security design**, aligned with enterprise Azure best practices.

The environment was intentionally designed to balance **technical depth, cost efficiency, and interview readiness**.

---

## Architecture Summary

**Topology**

* Hub VNet (Connectivity layer)
* Spoke VNet (Workload – NonProd)
* Hub ↔ Spoke peering
* User Defined Routes (UDRs) forcing egress through the hub
* Azure Firewall **Policy-first** security model (firewall instance not deployed to control cost)

**IP Design**

* Hub VNet: `10.0.0.0/16`
* Spoke VNet: `10.1.0.0/16`
* Workload Subnet: `10.1.0.0/24`

---

## Governance & Management

**Management Groups**

* Root
* Platform
* Landing Zones
* Workload (NonProd)

**Azure Policy**

* Required resource tags enforced at subscription scope:

  * `Owner`
  * `Environment`
  * `Application`

This ensures governance, cost attribution, and ownership tracking from resource creation.

---

## Networking

**Hub-and-Spoke Design**

* VNet peering configured with forwarded traffic allowed
* No direct internet egress from spoke workloads

**User Defined Routes**

* Default route (`0.0.0.0/0`) defined on the spoke subnet
* Next hop configured as a virtual appliance in the hub
* Azure system internet route overridden

**Routing Validation**

* A test VM was deployed to create a NIC
* Effective Routes were validated at the NIC level
* Confirmed that:

  * Azure default internet route is invalid
  * User-defined route forwards traffic toward the hub

---

## Security (Policy-First Firewall Design)

An **Azure Firewall Policy** was created to demonstrate centralized, scalable security governance without deploying a full firewall instance.

**Firewall Policy Components**

* Rule Collection Group: `rcg-nonprod-egress`
* Network Rule Collection:

  * DNS / NTP egress
* Application Rule Collection:

  * OS and package update endpoints (FQDN-based)

This reflects a **policy-first approach**, allowing security rules to be designed, reviewed, and versioned independently of enforcement infrastructure.

---

## Cost Management

Cost-aware decisions were intentionally applied:

* Azure Spot VM used for testing
* VM deallocated after validation
* No firewall runtime deployed
* No always-on compute resources

This approach enables architectural validation without unnecessary cloud spend.

---

## Validation Evidence

The following validations were performed:

* Hub ↔ Spoke peering connectivity
* UDR enforcement
* Runtime route validation via **Effective Routes**
* Governance enforcement via Azure Policy

Screenshots are included in the `/architecture` directory.

---

## Interview Walkthrough

During an interview, this project can be presented as:

1. Governance first (management groups + policy)
2. Network segmentation (hub-and-spoke)
3. Traffic control (UDRs)
4. Security design (firewall policy)
5. Runtime validation
6. Cost optimization decisions

---

## Notes

This repository documents architecture, configuration decisions, and validation steps.
Full live walkthroughs and extensions (e.g., Azure Firewall deployment) can be demonstrated during an interview if required.

---
