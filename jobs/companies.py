"""
Company data and market insights for job search (2025 Edition)
Source references: analyticsindiamag.com, forbesindia.com, india-briefing.com, nucamp.co, reviewadda.com, CIO.com
"""

FEATURED_COMPANIES = {
    "global_tech": [
        {
            "name": "Google (Alphabet)",
            "icon": "fab fa-google",
            "color": "#4285F4",
            "careers_url": "https://careers.google.com",
            "description": "Leading global tech company specializing in AI, search, ads, and cloud.",
            "categories": ["AI/ML", "Cloud", "Search", "Data Science"],
            "hq": "Mountain View, USA",
            "status": "Public"
        },
        {
            "name": "Microsoft",
            "icon": "fab fa-microsoft",
            "color": "#00A4EF",
            "careers_url": "https://careers.microsoft.com",
            "description": "Global software and cloud giant driving AI, productivity, and enterprise tools.",
            "categories": ["Software", "Cloud", "AI/ML", "Enterprise"],
            "hq": "Redmond, USA",
            "status": "Public"
        },
        {
            "name": "Amazon",
            "icon": "fab fa-amazon",
            "color": "#FF9900",
            "careers_url": "https://www.amazon.jobs",
            "description": "E-commerce, cloud computing, and AI leader.",
            "categories": ["Cloud", "Retail", "Operations", "AI/ML"],
            "hq": "Seattle, USA",
            "status": "Public"
        },
        {
            "name": "Apple",
            "icon": "fab fa-apple",
            "color": "#555555",
            "careers_url": "https://www.apple.com/careers",
            "description": "Consumer technology leader known for design and innovation.",
            "categories": ["Hardware", "Software", "Design", "AI/ML"],
            "hq": "Cupertino, USA",
            "status": "Public"
        },
        {
            "name": "NVIDIA",
            "icon": "fas fa-microchip",
            "color": "#76B900",
            "careers_url": "https://www.nvidia.com/en-us/about-nvidia/careers/",
            "description": "Pioneer in AI hardware, GPUs, and accelerated computing.",
            "categories": ["AI/ML", "Hardware", "Compute", "Infrastructure"],
            "hq": "Santa Clara, USA",
            "status": "Public"
        },
        {
            "name": "OpenAI",
            "icon": "fas fa-robot",
            "color": "#1E1E1E",
            "careers_url": "https://openai.com/careers",
            "description": "AI research and deployment company behind ChatGPT and GPT models.",
            "categories": ["AI/ML", "Research", "LLMs"],
            "hq": "San Francisco, USA",
            "status": "Private"
        },
        {
            "name": "Netflix",
            "icon": "fas fa-play-circle",
            "color": "#E50914",
            "careers_url": "https://jobs.netflix.com/",
            "description": "Entertainment & technology company specializing in streaming and AI-driven recommendations.",
            "categories": ["Software", "AI/ML", "Entertainment"],
            "hq": "Los Gatos, USA",
            "status": "Public"
        },
        {
            "name": "Stripe",
            "icon": "fas fa-credit-card",
            "color": "#635BFF",
            "careers_url": "https://stripe.com/jobs",
            "description": "Fintech company building economic infrastructure for the internet.",
            "categories": ["Fintech", "Payments", "APIs", "Infrastructure"],
            "hq": "San Francisco, USA",
            "status": "Private"
        }
    ],

    "indian_tech": [
        {
            "name": "TCS (Tata Consultancy Services)",
            "icon": "fas fa-building",
            "color": "#0070C0",
            "careers_url": "https://www.tcs.com/careers",
            "description": "India’s largest IT services and consulting company.",
            "categories": ["IT Services", "Consulting", "Digital"],
            "hq": "Mumbai, India",
            "status": "Public"
        },
        {
            "name": "Infosys",
            "icon": "fas fa-building",
            "color": "#007CC3",
            "careers_url": "https://www.infosys.com/careers",
            "description": "Global leader in digital services and consulting.",
            "categories": ["IT Services", "Cloud", "Consulting"],
            "hq": "Bengaluru, India",
            "status": "Public"
        },
        {
            "name": "Wipro",
            "icon": "fas fa-building",
            "color": "#341F65",
            "careers_url": "https://careers.wipro.com",
            "description": "Global information technology, consulting and business process services company.",
            "categories": ["IT Services", "Consulting", "Digital"],
            "hq": "Bengaluru, India",
            "status": "Public"
        },
        {
            "name": "HCLTech",
            "icon": "fas fa-building",
            "color": "#0075C9",
            "careers_url": "https://www.hcltech.com/careers",
            "description": "Engineering and technology services company.",
            "categories": ["IT Services", "Engineering", "Digital"],
            "hq": "Noida, India",
            "status": "Public"
        },
        {
            "name": "Zoho",
            "icon": "fas fa-cloud",
            "color": "#0E2F44",
            "careers_url": "https://www.zoho.com/careers",
            "description": "Bootstrapped SaaS company providing business productivity software.",
            "categories": ["SaaS", "Cloud", "Enterprise Tools"],
            "hq": "Chennai, India",
            "status": "Private"
        },
        {
            "name": "Flipkart",
            "icon": "fas fa-shopping-cart",
            "color": "#FF6F00",
            "careers_url": "https://www.flipkartcareers.com/",
            "description": "India’s leading e-commerce and logistics company.",
            "categories": ["Retail Tech", "E-commerce", "Logistics"],
            "hq": "Bengaluru, India",
            "status": "Private"
        }
    ],

    "global_consulting": [
        {
            "name": "Accenture",
            "icon": "fas fa-briefcase",
            "color": "#A100FF",
            "careers_url": "https://www.accenture.com/careers",
            "description": "Global professional services firm providing consulting and digital transformation.",
            "categories": ["Consulting", "Technology", "Cloud", "AI"],
            "hq": "Dublin, Ireland",
            "status": "Public"
        },
        {
            "name": "IBM",
            "icon": "fas fa-server",
            "color": "#1F70C1",
            "careers_url": "https://www.ibm.com/careers",
            "description": "Global leader in AI, hybrid cloud, and consulting.",
            "categories": ["Cloud", "AI/ML", "Software", "Consulting"],
            "hq": "New York, USA",
            "status": "Public"
        },
        {
            "name": "Cognizant",
            "icon": "fas fa-building",
            "color": "#1299D8",
            "careers_url": "https://careers.cognizant.com",
            "description": "IT services and digital transformation company.",
            "categories": ["IT Services", "Digital", "Consulting"],
            "hq": "New Jersey, USA / Chennai, India",
            "status": "Public"
        },
        {
            "name": "Capgemini",
            "icon": "fas fa-people-carry",
            "color": "#00ADEF",
            "careers_url": "https://www.capgemini.com/careers",
            "description": "Consulting and digital transformation company.",
            "categories": ["Consulting", "Digital", "IT Services"],
            "hq": "Paris, France",
            "status": "Public"
        },
        {
            "name": "Deloitte",
            "icon": "fas fa-handshake",
            "color": "#86BC25",
            "careers_url": "https://www2.deloitte.com/global/en/careers.html",
            "description": "One of the Big Four providing consulting, advisory, and tech services.",
            "categories": ["Consulting", "Finance", "Technology"],
            "hq": "New York, USA",
            "status": "Private"
        }
    ]
}


JOB_MARKET_INSIGHTS = {
    "trending_skills": [
        {"name": "Generative AI / LLMs", "growth": "+60%", "icon": "fas fa-robot"},
        {"name": "Cloud & Multi-Cloud", "growth": "+40%", "icon": "fas fa-cloud"},
        {"name": "MLOps / ML Engineering", "growth": "+35%", "icon": "fas fa-cogs"},
        {"name": "Data Engineering & Pipelines", "growth": "+32%", "icon": "fas fa-database"},
        {"name": "Cybersecurity & Privacy", "growth": "+30%", "icon": "fas fa-shield-alt"},
        {"name": "Platform Engineering / SRE / DevOps", "growth": "+28%", "icon": "fas fa-server"},
        {"name": "Edge / IoT / Embedded AI", "growth": "+22%", "icon": "fas fa-microchip"},
        {"name": "AI Governance / Explainability", "growth": "+18%", "icon": "fas fa-balance-scale"},
        {"name": "Domain AI (Health / Fintech / Legal)", "growth": "+15%", "icon": "fas fa-chart-line"}
    ],

    "top_locations": [
        {"name": "Bengaluru", "jobs": "60,000+", "icon": "fas fa-city"},
        {"name": "Hyderabad", "jobs": "45,000+", "icon": "fas fa-city"},
        {"name": "Pune", "jobs": "35,000+", "icon": "fas fa-city"},
        {"name": "Delhi NCR", "jobs": "30,000+", "icon": "fas fa-city"},
        {"name": "Chennai", "jobs": "25,000+", "icon": "fas fa-city"},
        {"name": "Mumbai", "jobs": "20,000+", "icon": "fas fa-city"},
        {"name": "Noida", "jobs": "15,000+", "icon": "fas fa-city"},
        {"name": "Remote / Global", "jobs": "10,000+", "icon": "fas fa-globe"}
    ],

    "salary_insights": [
        {"role": "AI / ML Engineer", "range": "₹20–45+ LPA / $120k–$300k", "experience": "2–6 years"},
        {"role": "Data Scientist", "range": "₹12–30 LPA / $110k–$220k", "experience": "2–5 years"},
        {"role": "Cloud / DevOps Engineer", "range": "₹10–28 LPA / $100k–$250k", "experience": "2–6 years"},
        {"role": "Full Stack Developer", "range": "₹8–25 LPA / $90k–$200k", "experience": "1–5 years"},
        {"role": "Cybersecurity Engineer", "range": "₹12–28 LPA / $120k–$240k", "experience": "2–5 years"},
        {"role": "Product Manager (Tech / AI)", "range": "₹15–40+ LPA / $130k–$300k", "experience": "3–7 years"},
        {"role": "MLOps / ML Infrastructure Engineer", "range": "₹18–40 LPA / $140k–$280k", "experience": "2–6 years"},
        {"role": "Software Architect / Lead Engineer", "range": "₹30–60+ LPA / $200k–$400k+", "experience": "5+ years"}
    ]
}


# ---------------- Helper Functions ---------------- #

def get_featured_companies(category=None):
    """Return featured companies by category or all companies."""
    if category and category in FEATURED_COMPANIES:
        return FEATURED_COMPANIES[category]
    return [company for companies in FEATURED_COMPANIES.values() for company in companies]


def get_market_insights():
    """Return global job market insights."""
    return JOB_MARKET_INSIGHTS


def get_company_info(company_name):
    """Return company info by name."""
    for companies in FEATURED_COMPANIES.values():
        for company in companies:
            if company["name"].lower() == company_name.lower():
                return company
    return None


def get_companies_by_industry(industry_keyword):
    """Return list of companies filtered by matching industry keyword."""
    result = []
    for companies_list in FEATURED_COMPANIES.values():
        for company in companies_list:
            if any(industry_keyword.lower() in cat.lower() for cat in company.get("categories", [])):
                result.append(company)
    return result
