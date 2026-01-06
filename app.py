import streamlit as st
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Azure Landing Zone - Hub & Spoke | Luis Santiago-Ramirez",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0078D4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #505050;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #0078D4;
        border-bottom: 2px solid #0078D4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .tech-badge {
        display: inline-block;
        background-color: #0078D4;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.85rem;
    }
    .evidence-container {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #fafafa;
    }
    .callout-box {
        background-color: #e7f3ff;
        border-left: 4px solid #0078D4;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .cost-highlight {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .architecture-diagram {
        background: linear-gradient(to bottom, #1a1a2e 0%, #16213e 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
    }
    .hub-box {
        background: linear-gradient(135deg, #0078D4 0%, #106EBE 100%);
        border-radius: 10px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    .spoke-box {
        background: linear-gradient(135deg, #5C2D91 0%, #8661C5 100%);
        border-radius: 10px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    .firewall-box {
        background: linear-gradient(135deg, #D83B01 0%, #EA4300 100%);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/1200px-Microsoft_Azure.svg.png", width=80)
    st.markdown("### Navigation")
    
    section = st.radio(
        "Go to Section:",
        ["🏠 Overview", "🏗️ Architecture", "🔐 Governance", "🌐 Networking", 
         "🛡️ Security", "💰 Cost Management", "✅ Validation", "👤 About Me"]
    )
    
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown("[📂 GitHub Repository](https://github.com/SantRamLAnt/azure-landing-zone-hub-spoke)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/luisantoniosantiago-ramirez-70b418196)")
    
    st.markdown("---")
    st.markdown("### Technologies Used")
    techs = ["Azure Landing Zone", "Hub-Spoke", "VNet Peering", "UDR", 
             "Azure Policy", "Firewall Policy", "RBAC", "Spot VMs"]
    for tech in techs:
        st.markdown(f"<span class='tech-badge'>{tech}</span>", unsafe_allow_html=True)

# Main content based on selection
if section == "🏠 Overview":
    st.markdown("<h1 class='main-header'>☁️ Azure Landing Zone</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Hub-and-Spoke Implementation | Enterprise Architecture Portfolio</p>", unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-value'>2</div>
            <div class='metric-label'>Virtual Networks</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='metric-card' style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);'>
            <div class='metric-value'>4</div>
            <div class='metric-label'>Management Groups</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='metric-card' style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);'>
            <div class='metric-value'>357</div>
            <div class='metric-label'>Policy Parameters</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class='metric-card' style='background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);'>
            <div class='metric-value'>$0</div>
            <div class='metric-label'>Idle Cost (Deallocated)</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project overview
    st.markdown("<h2 class='section-header'>Project Overview</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='callout-box'>
    <strong>🎯 Purpose:</strong> This project demonstrates a production-ready Azure Landing Zone implementation 
    using hub-and-spoke network topology, aligned with Microsoft's Cloud Adoption Framework (CAF) and 
    enterprise best practices.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎯 What This Demonstrates")
        st.markdown("""
        - **Governance-first approach** with Management Groups and Azure Policy
        - **Network segmentation** using hub-and-spoke topology
        - **Controlled egress routing** via User Defined Routes (UDRs)
        - **Policy-first security** with Azure Firewall Policy
        - **Cost optimization** with Spot VMs and resource deallocation
        - **Runtime validation** proving the architecture works
        """)
    
    with col2:
        st.markdown("#### 🛠️ Technologies & Skills")
        st.markdown("""
        - Azure Virtual Networks & Peering
        - Azure Policy & RBAC
        - User Defined Routes (UDRs)
        - Azure Firewall Policy
        - Management Groups & Subscriptions
        - Cost Management & Tagging Strategy
        - Infrastructure Validation
        """)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>Architecture at a Glance</h2>", unsafe_allow_html=True)
    
    # Visual architecture representation
    st.markdown("""
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
    """)

elif section == "🏗️ Architecture":
    st.markdown("<h1 class='main-header'>🏗️ Architecture Design</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>Hub-and-Spoke Topology</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='hub-box'>
            <h3>🔷 HUB VNET</h3>
            <p><strong>vnet-hub-eastus</strong></p>
            <p>10.0.0.0/16</p>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>Centralized connectivity & security services</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Hub Components:**
        - Connectivity subscription
        - Azure Firewall Policy
        - Central routing control
        - Shared services subnet
        """)
    
    with col2:
        st.markdown("""
        <div class='spoke-box'>
            <h3>🔶 SPOKE VNET</h3>
            <p><strong>vnet-spoke-nonprod-eastus</strong></p>
            <p>10.1.0.0/16</p>
            <hr style='border-color: rgba(255,255,255,0.3);'>
            <p>Workload isolation & segmentation</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Spoke Components:**
        - Workload subscription
        - Workload subnet (10.1.0.0/24)
        - Test VM (vm-test-spoke-01)
        - UDR forcing traffic to hub
        """)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 Azure Portal Evidence: VNet Peering</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='callout-box'>
    <strong>✅ Validation:</strong> VNet peering is configured and connected between hub and spoke, 
    enabling seamless network communication while maintaining segmentation.
    </div>
    """, unsafe_allow_html=True)
    
    # Display peering screenshot
    try:
        st.image("architecture/networkingpeer.png", caption="VNet Peering Configuration - spoke-to-hub (Connected)", use_container_width=True)
    except:
        st.info("📷 Screenshot: VNet Peering showing 'spoke-to-hub' peering state as Connected")
    
    st.markdown("""
    **Key Peering Settings:**
    - Peering link name: `spoke-to-hub`
    - Peering state: ✅ **Connected**
    - Allow hub to access spoke: ✅ Enabled
    - Traffic forwarding configured for controlled routing
    """)

elif section == "🔐 Governance":
    st.markdown("<h1 class='main-header'>🔐 Governance & Policy</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>Management Group Hierarchy</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    ```
    📁 Root Management Group
    └── 📁 Platform
        └── 📁 Landing Zones
            └── 📁 Workload (NonProd)
                └── 📋 lz-workload-nonprod (Subscription)
    ```
    """)
    
    st.markdown("""
    <div class='callout-box'>
    <strong>🎯 Design Decision:</strong> Management groups enable hierarchical policy inheritance, 
    ensuring governance controls flow down to all subscriptions and resources automatically.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>Azure Policy Enforcement</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Required Resource Tags")
        st.markdown("""
        | Tag Name | Purpose | Example Value |
        |----------|---------|---------------|
        | `Owner` | Accountability | Luis Ramirez |
        | `Environment` | Lifecycle stage | NonProd |
        | `Application` | Workload identity | Workload / Connectivity |
        """)
    
    with col2:
        st.markdown("#### Policy Stats")
        st.metric("Total Parameters", "357")
        st.metric("Policy Type", "Initiative")
        st.metric("Scope", "Subscription")
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 Azure Portal Evidence: Policy Assignment</h2>", unsafe_allow_html=True)
    
    try:
        st.image("architecture/azurepolicyrequired.png", caption="ASC Default Policy Assignment - 357 Parameters Configured", use_container_width=True)
    except:
        st.info("📷 Screenshot: Azure Policy showing ASC Default initiative with 357 parameters")
    
    st.markdown("""
    **Policy Enforcement Benefits:**
    - ✅ Consistent tagging across all resources
    - ✅ Cost attribution and chargeback capability
    - ✅ Clear ownership and accountability
    - ✅ Automated compliance monitoring
    """)

elif section == "🌐 Networking":
    st.markdown("<h1 class='main-header'>🌐 Networking & Routing</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>User Defined Routes (UDR)</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='callout-box'>
    <strong>🔒 Security Control:</strong> All spoke traffic is forced through the hub via UDR, 
    enabling centralized inspection and control of egress traffic.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Route Table: `rt-spoke-nonprod`")
    
    st.markdown("""
    | Route Name | Address Prefix | Next Hop Type | Next Hop Address |
    |------------|---------------|---------------|------------------|
    | `default-to-hub` | 0.0.0.0/0 | Virtual Appliance | 10.0.0.4 |
    """)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 Azure Portal Evidence: UDR Configuration</h2>", unsafe_allow_html=True)
    
    try:
        st.image("architecture/networkingudr.png", caption="User Defined Route - default-to-hub forcing all traffic to hub", use_container_width=True)
    except:
        st.info("📷 Screenshot: UDR configuration showing 0.0.0.0/0 → 10.0.0.4")
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 Effective Routes Validation</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='cost-highlight'>
    <strong>✅ Runtime Proof:</strong> Effective routes on the VM NIC confirm that the UDR is working - 
    Azure's default internet route is marked as <strong>Invalid</strong> and our custom route is <strong>Active</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    try:
        st.image("architecture/VMRoute.png", caption="Effective Routes showing UDR enforcement - Azure internet route Invalid, User route Active", use_container_width=True)
    except:
        st.info("📷 Screenshot: Effective Routes validation")
    
    st.markdown("""
    **Effective Routes Analysis:**
    | Source | State | Address Prefix | Next Hop Type | Next Hop IP | Route Name |
    |--------|-------|----------------|---------------|-------------|------------|
    | Default | Active | 10.1.0.0/16 | Virtual network | - | - |
    | Default | Active | 10.0.0.0/16 | VNet peering | - | - |
    | Default | **Invalid** | 0.0.0.0/0 | Internet | - | - |
    | **User** | **Active** | 0.0.0.0/0 | None | 10.0.0.4 | default-to-hub |
    
    ✅ This proves egress traffic from the spoke is forced through the hub!
    """)

elif section == "🛡️ Security":
    st.markdown("<h1 class='main-header'>🛡️ Security Design</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>Policy-First Firewall Approach</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='callout-box'>
    <strong>💡 Design Decision:</strong> Azure Firewall Policy was created to demonstrate security governance 
    without deploying a full firewall instance (which costs ~$900/month). This shows the <strong>policy-first</strong> 
    approach where rules can be designed, reviewed, and version-controlled independently.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='firewall-box'>
            <h4>🔥 Firewall Policy</h4>
            <p>FirewallPolicies</p>
            <p>Tier: Standard</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Policy Configuration:**
        - Resource Group: `rg-connectivity-hub`
        - Location: East US
        - Policy Tier: Standard
        - Rules: 2 configured
        """)
    
    with col2:
        st.markdown("#### Rule Collections")
        st.markdown("""
        **Rule Collection Group:** `rcg-nonprod-egress`
        
        **Network Rules:**
        - DNS egress (UDP 53)
        - NTP egress (UDP 123)
        
        **Application Rules:**
        - OS update endpoints (FQDN-based)
        - Package repository access
        """)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 Azure Portal Evidence: Firewall Policy</h2>", unsafe_allow_html=True)
    
    try:
        st.image("architecture/securityfirewall.png", caption="Azure Firewall Policy with Policy Analytics", use_container_width=True)
    except:
        st.info("📷 Screenshot: Firewall Policy configuration")
    
    st.markdown("""
    **Security Benefits:**
    - ✅ Centralized security rule management
    - ✅ Version-controlled policy changes
    - ✅ Scalable to multiple firewalls
    - ✅ Cost-effective design validation
    """)

elif section == "💰 Cost Management":
    st.markdown("<h1 class='main-header'>💰 Cost Management</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>Cost-Aware Design Decisions</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='cost-highlight'>
    <strong>💵 Philosophy:</strong> Enterprise architecture can be demonstrated without enterprise costs. 
    This project validates technical concepts while minimizing cloud spend.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### ✅ Azure Spot VM")
        st.markdown("""
        - Up to **90% savings** vs on-demand
        - Perfect for non-production testing
        - Eviction policy: Deallocate
        - Used for route validation
        """)
    
    with col2:
        st.markdown("#### ✅ VM Deallocation")
        st.markdown("""
        - VM stopped when not in use
        - **$0 compute cost** when idle
        - Storage cost only (~$5/month)
        - Start on-demand for demos
        """)
    
    with col3:
        st.markdown("#### ✅ No Firewall Runtime")
        st.markdown("""
        - Firewall Policy created (free)
        - No firewall instance deployed
        - **Saves ~$900/month**
        - Can deploy for production
        """)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 Azure Portal Evidence: Deallocated VM</h2>", unsafe_allow_html=True)
    
    try:
        st.image("architecture/costvmdeallocated.png", caption="VM Status: Stopped (deallocated) - Zero compute cost", use_container_width=True)
    except:
        st.info("📷 Screenshot: VM showing deallocated status")
    
    st.markdown("""
    **VM Configuration Details:**
    | Property | Value |
    |----------|-------|
    | Name | vm-test-spoke-01 |
    | Status | **Stopped (deallocated)** |
    | Size | Standard D2s v3 (2 vCPU, 8 GB) |
    | OS | Linux (Ubuntu 24.04) |
    | Azure Spot | ✅ Capacity (Deallocate on eviction) |
    | Tags | Owner: Luis Ramirez, Environment: NonProd |
    """)
    
    st.markdown("---")
    st.markdown("#### 💡 Interview Talking Point")
    st.markdown("""
    > *"I intentionally designed this environment to validate enterprise architecture patterns 
    > without unnecessary cloud spend. The Spot VM with deallocation policy, combined with 
    > policy-first firewall design, demonstrates that I think about cost optimization from 
    > day one—not as an afterthought."*
    """)

elif section == "✅ Validation":
    st.markdown("<h1 class='main-header'>✅ Validation & Evidence</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-header'>Validation Checklist</h2>", unsafe_allow_html=True)
    
    validations = [
        ("Hub ↔ Spoke VNet Peering", "Connected", "✅"),
        ("UDR Applied to Spoke Subnet", "Active", "✅"),
        ("Azure Default Internet Route", "Invalid (Overridden)", "✅"),
        ("Custom Route to Hub", "Active", "✅"),
        ("Azure Policy Enforcement", "357 Parameters", "✅"),
        ("Resource Tagging", "Owner, Environment, Application", "✅"),
        ("Firewall Policy Created", "2 Rules Configured", "✅"),
        ("Cost Optimization", "Spot VM, Deallocated", "✅"),
    ]
    
    for item, status, check in validations:
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.markdown(f"**{item}**")
        with col2:
            st.markdown(f"`{status}`")
        with col3:
            st.markdown(f"<span style='font-size: 1.5rem;'>{check}</span>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h2 class='section-header'>📸 All Evidence Screenshots</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🌐 Networking", "🔒 Routes", "🔐 Policy", "🛡️ Firewall", "💰 Cost"])
    
    with tab1:
        try:
            st.image("architecture/networkingpeer.png", caption="VNet Peering - Connected", use_container_width=True)
        except:
            st.info("VNet Peering Screenshot")
    
    with tab2:
        try:
            st.image("architecture/VMRoute.png", caption="Effective Routes - UDR Validated", use_container_width=True)
            st.image("architecture/networkingudr.png", caption="UDR Configuration", use_container_width=True)
        except:
            st.info("Route Screenshots")
    
    with tab3:
        try:
            st.image("architecture/azurepolicyrequired.png", caption="Azure Policy Assignment", use_container_width=True)
        except:
            st.info("Policy Screenshot")
    
    with tab4:
        try:
            st.image("architecture/securityfirewall.png", caption="Firewall Policy", use_container_width=True)
        except:
            st.info("Firewall Screenshot")
    
    with tab5:
        try:
            st.image("architecture/costvmdeallocated.png", caption="VM Deallocated for Cost Savings", use_container_width=True)
        except:
            st.info("Cost Screenshot")

elif section == "👤 About Me":
    st.markdown("<h1 class='main-header'>👤 About the Author</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;'>
            <h2>Luis Antonio<br>Santiago-Ramirez</h2>
            <p>Cloud Platform Engineer</p>
            <p>Eversource Energy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Professional Background")
        st.markdown("""
        **Current Role:** GIS Associate Technician at Eversource Energy
        
        **Experience:** 6+ years in utility infrastructure operations across gas, water, sewer, and electric systems
        
        **Focus:** Transitioning into Cloud Platform Engineering with emphasis on Azure architecture, 
        Infrastructure as Code, and DevSecOps practices
        """)
        
        st.markdown("### Education")
        st.markdown("""
        - 🎓 **M.Eng Computer Engineering** - Dartmouth College (Pursuing, Spring 2026)
        - 🎓 **B.S. Geography (Regional Planning)** - Westfield State University, 2019
          - Minor: Geographic Information Systems (GIS)
        """)
    
    st.markdown("---")
    st.markdown("### Azure Certifications")
    
    cert_col1, cert_col2, cert_col3, cert_col4 = st.columns(4)
    
    with cert_col1:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background-color: #e7f3ff; border-radius: 10px;'>
            <p style='font-size: 2rem;'>🔒</p>
            <p><strong>AZ-500</strong></p>
            <p style='font-size: 0.8rem;'>Security Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col2:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background-color: #e7f3ff; border-radius: 10px;'>
            <p style='font-size: 2rem;'>🔄</p>
            <p><strong>AZ-400</strong></p>
            <p style='font-size: 0.8rem;'>DevOps Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col3:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background-color: #e7f3ff; border-radius: 10px;'>
            <p style='font-size: 2rem;'>🤖</p>
            <p><strong>AI-102</strong></p>
            <p style='font-size: 0.8rem;'>AI Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cert_col4:
        st.markdown("""
        <div style='text-align: center; padding: 1rem; background-color: #e7f3ff; border-radius: 10px;'>
            <p style='font-size: 2rem;'>📊</p>
            <p><strong>DP-203</strong></p>
            <p style='font-size: 0.8rem;'>Data Engineer</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Why I Built This Project")
    st.markdown("""
    <div class='callout-box'>
    <em>"I built this Azure Landing Zone outside of work hours, using my own resources, to demonstrate 
    that I can design and implement enterprise-grade cloud infrastructure. Every component—from management 
    groups to firewall policies—reflects real-world best practices I've studied through Microsoft Learn, 
    Coursera, and hands-on experimentation. This isn't just a lab exercise; it's proof that I'm ready 
    to contribute to Eversource's cloud platform initiatives from day one."</em>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Connect With Me")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[📂 GitHub](https://github.com/SantRamLAnt)")
    with col2:
        st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/luisantoniosantiago-ramirez-70b418196)")
    with col3:
        st.markdown("📧 lasrsecond@gmail.com")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 1rem;'>
    <p>Azure Landing Zone Portfolio | Built by Luis Santiago-Ramirez | 2026</p>
    <p style='font-size: 0.8rem;'>This project was developed independently outside of work hours using personal resources.<br>
    No Eversource data or systems were used.</p>
</div>
""", unsafe_allow_html=True)
