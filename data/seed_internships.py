"""
One-time seed script to populate the Supabase internships table with 50 records.
Run: python seed_internships.py
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from supabase import create_client
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

INTERNSHIPS = [
    # --- Software Engineering ---
    {
        "company": "Google",
        "role": "Software Engineering Intern",
        "required_skills": ["Python", "Data Structures", "Algorithms", "OOP"],
        "preferred_skills": ["Go", "Distributed Systems", "System Design"],
        "location": "Bangalore, India",
        "stipend": "₹1,50,000/month",
        "description": "Work on Google's core infrastructure, contributing to large-scale distributed systems that serve billions of users. You'll solve complex engineering problems alongside some of the best engineers in the world.",
        "apply_link": "https://careers.google.com/students/"
    },
    {
        "company": "Microsoft",
        "role": "Software Engineer Intern",
        "required_skills": ["C#", "Azure", "REST APIs", "Git"],
        "preferred_skills": ["TypeScript", "React", "Kubernetes"],
        "location": "Hyderabad, India",
        "stipend": "₹1,20,000/month",
        "description": "Join Microsoft's Azure team and build cloud-native services used by enterprises worldwide. You'll contribute to real features shipped to millions of customers.",
        "apply_link": "https://careers.microsoft.com/students/us/en/usuniversityinternship"
    },
    {
        "company": "Amazon",
        "role": "SDE Intern",
        "required_skills": ["Java", "Data Structures", "Algorithms", "SQL"],
        "preferred_skills": ["AWS", "Python", "Microservices"],
        "location": "Hyderabad, India",
        "stipend": "₹1,00,000/month",
        "description": "Build and own features for Amazon's e-commerce platform. Interns are treated like full SDEs and are expected to design, implement, and deliver real customer-facing features.",
        "apply_link": "https://amazon.jobs/en/teams/internships-for-students"
    },
    {
        "company": "Flipkart",
        "role": "Software Development Intern",
        "required_skills": ["Java", "Spring Boot", "MySQL", "REST APIs"],
        "preferred_skills": ["Kafka", "Redis", "Docker"],
        "location": "Bangalore, India",
        "stipend": "₹80,000/month",
        "description": "Contribute to India's largest e-commerce platform. Work on high-traffic backend systems handling millions of transactions daily during sale events.",
        "apply_link": "https://www.flipkartcareers.com/"
    },
    {
        "company": "Razorpay",
        "role": "Backend Engineering Intern",
        "required_skills": ["Node.js", "PostgreSQL", "REST APIs", "Git"],
        "preferred_skills": ["Redis", "Docker", "AWS", "TypeScript"],
        "location": "Bangalore, India",
        "stipend": "₹70,000/month",
        "description": "Build the financial infrastructure of India. Work on payment processing, banking APIs, and fintech products that power over 8 million businesses.",
        "apply_link": "https://razorpay.com/jobs/"
    },
    {
        "company": "Zepto",
        "role": "Software Engineer Intern",
        "required_skills": ["Python", "FastAPI", "PostgreSQL", "Docker"],
        "preferred_skills": ["Kubernetes", "Redis", "System Design"],
        "location": "Mumbai, India",
        "stipend": "₹75,000/month",
        "description": "Help build and scale Zepto's 10-minute delivery platform. Work on real-time inventory, delivery routing, and order management systems.",
        "apply_link": "https://www.zepto.team/jobs"
    },
    {
        "company": "Swiggy",
        "role": "Backend Developer Intern",
        "required_skills": ["Go", "Microservices", "PostgreSQL", "REST APIs"],
        "preferred_skills": ["Kafka", "Redis", "Docker", "Kubernetes"],
        "location": "Bangalore, India",
        "stipend": "₹85,000/month",
        "description": "Work on Swiggy's hyperlocal delivery platform. Build APIs and services that handle millions of orders and real-time location tracking.",
        "apply_link": "https://careers.swiggy.com/"
    },
    {
        "company": "PhonePe",
        "role": "Software Engineering Intern",
        "required_skills": ["Java", "Spring Boot", "MySQL", "Microservices"],
        "preferred_skills": ["Kafka", "Redis", "AWS"],
        "location": "Bangalore, India",
        "stipend": "₹90,000/month",
        "description": "Build the digital payments infrastructure used by 500 million Indians. Work on UPI, wallet, and payment processing systems with extremely high availability requirements.",
        "apply_link": "https://www.phonepe.com/careers/"
    },
    {
        "company": "CRED",
        "role": "Full Stack Intern",
        "required_skills": ["React", "Node.js", "TypeScript", "REST APIs"],
        "preferred_skills": ["GraphQL", "PostgreSQL", "Redis"],
        "location": "Bangalore, India",
        "stipend": "₹65,000/month",
        "description": "Build premium fintech experiences for India's creditworthy population. Work on CRED's app, web platform, and backend APIs serving millions of users.",
        "apply_link": "https://careers.cred.club/"
    },
    {
        "company": "Meesho",
        "role": "Software Development Intern",
        "required_skills": ["Python", "Django", "MySQL", "Git"],
        "preferred_skills": ["React", "Docker", "AWS"],
        "location": "Bangalore, India",
        "stipend": "₹60,000/month",
        "description": "Help democratize internet commerce for the next billion users. Work on supplier tools, catalog management, and logistics systems.",
        "apply_link": "https://meesho.io/careers"
    },
    # --- Frontend / UI ---
    {
        "company": "Zomato",
        "role": "Frontend Engineer Intern",
        "required_skills": ["React", "JavaScript", "HTML", "CSS", "TypeScript"],
        "preferred_skills": ["Next.js", "GraphQL", "Performance Optimization"],
        "location": "Gurugram, India",
        "stipend": "₹70,000/month",
        "description": "Build beautiful, performant user interfaces for Zomato's food delivery and dining-out products used by millions of customers daily.",
        "apply_link": "https://www.zomato.com/careers"
    },
    {
        "company": "Nykaa",
        "role": "Frontend Developer Intern",
        "required_skills": ["React", "JavaScript", "CSS", "Redux"],
        "preferred_skills": ["Next.js", "TypeScript", "Tailwind CSS"],
        "location": "Mumbai, India",
        "stipend": "₹55,000/month",
        "description": "Build the shopping experience for India's leading beauty and fashion platform. Work on product listing, checkout flows, and personalization features.",
        "apply_link": "https://careers.nykaa.com/"
    },
    {
        "company": "Urban Company",
        "role": "React Developer Intern",
        "required_skills": ["React", "JavaScript", "REST APIs", "HTML/CSS"],
        "preferred_skills": ["React Native", "TypeScript", "Firebase"],
        "location": "Gurugram, India",
        "stipend": "₹50,000/month",
        "description": "Build the consumer-facing app and web experiences for Urban Company's home services platform operating across 30+ cities.",
        "apply_link": "https://www.urbancompany.com/careers"
    },
    # --- Machine Learning / AI ---
    {
        "company": "Google DeepMind",
        "role": "ML Research Intern",
        "required_skills": ["Python", "TensorFlow", "Machine Learning", "Linear Algebra", "Statistics"],
        "preferred_skills": ["PyTorch", "Research Papers", "NLP", "Computer Vision"],
        "location": "Bangalore, India",
        "stipend": "₹2,00,000/month",
        "description": "Conduct cutting-edge AI research at one of the world's leading AI labs. Work on foundation models, reinforcement learning, or scientific AI applications.",
        "apply_link": "https://deepmind.google/careers/"
    },
    {
        "company": "Microsoft Research",
        "role": "AI Research Intern",
        "required_skills": ["Python", "PyTorch", "Machine Learning", "Statistics"],
        "preferred_skills": ["NLP", "Computer Vision", "Research Experience"],
        "location": "Bangalore, India",
        "stipend": "₹1,50,000/month",
        "description": "Work alongside world-class researchers on applied AI and machine learning projects. Publish papers and contribute to Microsoft's AI products.",
        "apply_link": "https://www.microsoft.com/en-us/research/academic-program/research-internship/"
    },
    {
        "company": "Lenskart",
        "role": "Machine Learning Intern",
        "required_skills": ["Python", "scikit-learn", "Pandas", "NumPy", "Machine Learning"],
        "preferred_skills": ["Computer Vision", "TensorFlow", "OpenCV"],
        "location": "Gurugram, India",
        "stipend": "₹60,000/month",
        "description": "Apply ML to improve product recommendations, virtual try-on features, and demand forecasting for India's largest eyewear brand.",
        "apply_link": "https://lenskart.com/careers"
    },
    {
        "company": "Ola",
        "role": "Data Science Intern",
        "required_skills": ["Python", "Pandas", "SQL", "Machine Learning", "Statistics"],
        "preferred_skills": ["Spark", "Airflow", "Tableau"],
        "location": "Bangalore, India",
        "stipend": "₹65,000/month",
        "description": "Use data to improve driver matching, surge pricing, ETA predictions, and ride safety for Ola's ride-hailing platform.",
        "apply_link": "https://ola.careers/"
    },
    {
        "company": "Paytm",
        "role": "AI/ML Intern",
        "required_skills": ["Python", "TensorFlow", "Pandas", "SQL", "Machine Learning"],
        "preferred_skills": ["NLP", "Fraud Detection", "AWS SageMaker"],
        "location": "Noida, India",
        "stipend": "₹55,000/month",
        "description": "Build ML models for fraud detection, credit risk scoring, and personalized recommendations on Paytm's fintech platform.",
        "apply_link": "https://paytm.com/careers"
    },
    {
        "company": "Inmobi",
        "role": "Machine Learning Intern",
        "required_skills": ["Python", "Machine Learning", "SQL", "Pandas"],
        "preferred_skills": ["AdTech", "Recommendation Systems", "Spark"],
        "location": "Bangalore, India",
        "stipend": "₹70,000/month",
        "description": "Work on ML models for ad targeting, user personalization, and click-through rate prediction serving billions of ad impressions.",
        "apply_link": "https://www.inmobi.com/company/careers/"
    },
    # --- Data Engineering ---
    {
        "company": "Walmart Global Tech",
        "role": "Data Engineering Intern",
        "required_skills": ["Python", "SQL", "Spark", "ETL", "Data Warehousing"],
        "preferred_skills": ["Airflow", "Kafka", "Hadoop", "Tableau"],
        "location": "Bangalore, India",
        "stipend": "₹80,000/month",
        "description": "Build data pipelines and analytics systems that power Walmart's global supply chain and retail operations across 10,000+ stores.",
        "apply_link": "https://careers.walmart.com/"
    },
    {
        "company": "Freshworks",
        "role": "Data Analyst Intern",
        "required_skills": ["SQL", "Python", "Excel", "Data Visualization"],
        "preferred_skills": ["Tableau", "Looker", "A/B Testing", "Statistics"],
        "location": "Chennai, India",
        "stipend": "₹50,000/month",
        "description": "Analyze product usage, customer behavior, and business metrics to help Freshworks make data-driven decisions for its SaaS products.",
        "apply_link": "https://www.freshworks.com/company/careers/"
    },
    # --- DevOps / Cloud ---
    {
        "company": "Infosys",
        "role": "DevOps Intern",
        "required_skills": ["Linux", "Docker", "Git", "CI/CD", "Bash"],
        "preferred_skills": ["Kubernetes", "Terraform", "AWS", "Jenkins"],
        "location": "Pune, India",
        "stipend": "₹35,000/month",
        "description": "Work on infrastructure automation, CI/CD pipelines, and cloud migration projects for enterprise clients across industries.",
        "apply_link": "https://www.infosys.com/careers/apply.html"
    },
    {
        "company": "Tata Consultancy Services",
        "role": "Cloud Engineering Intern",
        "required_skills": ["AWS", "Linux", "Python", "Docker", "Git"],
        "preferred_skills": ["Terraform", "Kubernetes", "Azure", "GCP"],
        "location": "Mumbai, India",
        "stipend": "₹30,000/month",
        "description": "Help clients migrate to cloud infrastructure and implement DevOps practices across TCS's global enterprise portfolio.",
        "apply_link": "https://ibegin.tcs.com/"
    },
    {
        "company": "Zoho",
        "role": "Site Reliability Engineering Intern",
        "required_skills": ["Linux", "Python", "Docker", "Monitoring", "Networking"],
        "preferred_skills": ["Kubernetes", "Prometheus", "Grafana", "Terraform"],
        "location": "Chennai, India",
        "stipend": "₹45,000/month",
        "description": "Maintain and improve the reliability, performance, and scalability of Zoho's cloud infrastructure serving 80 million+ users.",
        "apply_link": "https://careers.zohocorp.com/"
    },
    # --- Mobile Development ---
    {
        "company": "Dream11",
        "role": "Android Developer Intern",
        "required_skills": ["Kotlin", "Android SDK", "REST APIs", "Git"],
        "preferred_skills": ["Jetpack Compose", "MVVM", "Firebase"],
        "location": "Mumbai, India",
        "stipend": "₹60,000/month",
        "description": "Build features for India's largest fantasy sports platform with 200M+ users. Work on real-time game updates, live scores, and contest management.",
        "apply_link": "https://dream11.com/careers"
    },
    {
        "company": "ShareChat",
        "role": "iOS Developer Intern",
        "required_skills": ["Swift", "iOS SDK", "REST APIs", "Git"],
        "preferred_skills": ["SwiftUI", "Objective-C", "Firebase"],
        "location": "Bangalore, India",
        "stipend": "₹55,000/month",
        "description": "Build features for ShareChat and Moj, India's largest vernacular social media platforms with 400M+ monthly active users.",
        "apply_link": "https://sharechat.com/careers"
    },
    {
        "company": "MX Player",
        "role": "React Native Intern",
        "required_skills": ["React Native", "JavaScript", "REST APIs"],
        "preferred_skills": ["TypeScript", "Redux", "Video Streaming"],
        "location": "Noida, India",
        "stipend": "₹50,000/month",
        "description": "Build cross-platform mobile features for MX Player's OTT streaming platform serving 280M+ monthly active users.",
        "apply_link": "https://www.mxplayer.in/careers"
    },
    # --- Product / Design ---
    {
        "company": "Groww",
        "role": "Product Engineer Intern",
        "required_skills": ["React", "TypeScript", "Node.js", "PostgreSQL"],
        "preferred_skills": ["System Design", "Product Thinking", "A/B Testing"],
        "location": "Bangalore, India",
        "stipend": "₹75,000/month",
        "description": "Work at the intersection of product and engineering at India's fastest-growing investment platform with 10M+ active investors.",
        "apply_link": "https://groww.in/p/careers"
    },
    {
        "company": "BharatPe",
        "role": "Full Stack Intern",
        "required_skills": ["React", "Node.js", "PostgreSQL", "REST APIs"],
        "preferred_skills": ["TypeScript", "Redis", "Docker"],
        "location": "New Delhi, India",
        "stipend": "₹65,000/month",
        "description": "Build merchant-facing fintech products that help 12M+ small businesses accept digital payments and access credit.",
        "apply_link": "https://bharatpe.com/careers"
    },
    # --- Cybersecurity ---
    {
        "company": "Quick Heal",
        "role": "Cybersecurity Intern",
        "required_skills": ["Python", "Networking", "Linux", "Security Fundamentals"],
        "preferred_skills": ["Malware Analysis", "Wireshark", "SIEM", "Penetration Testing"],
        "location": "Pune, India",
        "stipend": "₹40,000/month",
        "description": "Work on threat intelligence, vulnerability research, and security product development at one of India's leading cybersecurity companies.",
        "apply_link": "https://www.quickheal.com/careers"
    },
    {
        "company": "Securonix",
        "role": "Security Engineering Intern",
        "required_skills": ["Python", "SQL", "Linux", "SIEM", "Networking"],
        "preferred_skills": ["Machine Learning", "Log Analysis", "SOAR"],
        "location": "Bangalore, India",
        "stipend": "₹55,000/month",
        "description": "Help build next-gen SIEM and security analytics products that protect Fortune 500 companies from cyber threats using AI.",
        "apply_link": "https://www.securonix.com/careers/"
    },
    # --- Blockchain / Web3 ---
    {
        "company": "CoinDCX",
        "role": "Blockchain Developer Intern",
        "required_skills": ["Solidity", "Python", "JavaScript", "Ethereum"],
        "preferred_skills": ["Web3.js", "Hardhat", "DeFi", "Smart Contracts"],
        "location": "Mumbai, India",
        "stipend": "₹60,000/month",
        "description": "Build smart contracts, DeFi protocols, and blockchain integrations for India's largest crypto exchange.",
        "apply_link": "https://coindcx.com/careers/"
    },
    # --- Game Development ---
    {
        "company": "Nazara Technologies",
        "role": "Game Developer Intern",
        "required_skills": ["Unity", "C#", "Game Development", "3D Math"],
        "preferred_skills": ["Unreal Engine", "Shader Programming", "Mobile Gaming"],
        "location": "Mumbai, India",
        "stipend": "₹45,000/month",
        "description": "Build mobile and PC games at India's leading gaming company. Work on gameplay systems, UI, and multiplayer features.",
        "apply_link": "https://www.nazara.com/careers"
    },
    # --- Research / Academia ---
    {
        "company": "IIT Bangalore AI Lab",
        "role": "Research Intern (NLP)",
        "required_skills": ["Python", "PyTorch", "NLP", "Machine Learning", "Research"],
        "preferred_skills": ["Transformers", "BERT", "Research Paper Writing"],
        "location": "Bangalore, India",
        "stipend": "₹25,000/month",
        "description": "Conduct NLP research on low-resource Indian languages. Work with PhD scholars on cutting-edge language models and publish research.",
        "apply_link": "https://www.iisc.ac.in/research/"
    },
    {
        "company": "ISRO",
        "role": "Software Intern",
        "required_skills": ["C", "Python", "Linux", "Embedded Systems"],
        "preferred_skills": ["Real-time Systems", "Signal Processing", "MATLAB"],
        "location": "Thiruvananthapuram, India",
        "stipend": "₹20,000/month",
        "description": "Contribute to India's space program by working on satellite software, ground station systems, or mission control applications.",
        "apply_link": "https://www.isro.gov.in/career.html"
    },
    # --- SaaS / Enterprise ---
    {
        "company": "Salesforce",
        "role": "Software Engineer Intern",
        "required_skills": ["Java", "JavaScript", "REST APIs", "Apex"],
        "preferred_skills": ["Lightning Web Components", "Heroku", "SQL"],
        "location": "Hyderabad, India",
        "stipend": "₹1,00,000/month",
        "description": "Build features for the world's #1 CRM platform. Work on Salesforce's core product, AppExchange, or Einstein AI features.",
        "apply_link": "https://careers.salesforce.com/en/students/"
    },
    {
        "company": "SAP Labs",
        "role": "Development Intern",
        "required_skills": ["Java", "JavaScript", "SQL", "REST APIs"],
        "preferred_skills": ["ABAP", "Cloud Foundry", "React"],
        "location": "Bangalore, India",
        "stipend": "₹70,000/month",
        "description": "Work on SAP's enterprise software suite, building solutions for finance, supply chain, HR, and analytics used by 90% of Fortune 500 companies.",
        "apply_link": "https://jobs.sap.com/go/StudentJobsIndia/3200001/"
    },
    {
        "company": "Adobe",
        "role": "Software Engineer Intern",
        "required_skills": ["Java", "Python", "REST APIs", "Algorithms"],
        "preferred_skills": ["Machine Learning", "C++", "Computer Vision", "JavaScript"],
        "location": "Noida, India",
        "stipend": "₹1,10,000/month",
        "description": "Work on Adobe's Creative Cloud or Experience Cloud products. Contribute to Photoshop, Premiere, or Adobe Analytics.",
        "apply_link": "https://adobe.design/careers/"
    },
    # --- Fintech ---
    {
        "company": "Jupiter Money",
        "role": "Backend Intern",
        "required_skills": ["Node.js", "PostgreSQL", "REST APIs", "Git"],
        "preferred_skills": ["TypeScript", "Redis", "Docker", "Kafka"],
        "location": "Bangalore, India",
        "stipend": "₹50,000/month",
        "description": "Build banking and personal finance APIs for Jupiter's neo-banking platform. Work on account management, payments, and smart money features.",
        "apply_link": "https://jupiter.money/careers/"
    },
    {
        "company": "Fi Money",
        "role": "Full Stack Intern",
        "required_skills": ["React", "TypeScript", "Node.js", "REST APIs"],
        "preferred_skills": ["React Native", "PostgreSQL", "Redis"],
        "location": "Bangalore, India",
        "stipend": "₹60,000/month",
        "description": "Build delightful banking experiences for Fi's salary account and investment platform targeting young professionals.",
        "apply_link": "https://fi.money/careers"
    },
    # --- EdTech ---
    {
        "company": "BYJU'S",
        "role": "Software Development Intern",
        "required_skills": ["Java", "Spring Boot", "MySQL", "REST APIs"],
        "preferred_skills": ["React", "AWS", "Redis"],
        "location": "Bangalore, India",
        "stipend": "₹40,000/month",
        "description": "Build learning management systems, content delivery, and gamification features for India's largest EdTech platform with 150M learners.",
        "apply_link": "https://byjus.com/careers/"
    },
    {
        "company": "Unacademy",
        "role": "Frontend Intern",
        "required_skills": ["React", "JavaScript", "HTML/CSS", "REST APIs"],
        "preferred_skills": ["TypeScript", "Next.js", "Video Integration"],
        "location": "Bangalore, India",
        "stipend": "₹45,000/month",
        "description": "Build live learning interfaces, video streaming features, and educator tools for Unacademy's online education platform.",
        "apply_link": "https://unacademy.com/careers"
    },
    {
        "company": "Physics Wallah",
        "role": "Android Intern",
        "required_skills": ["Kotlin", "Android SDK", "REST APIs", "Firebase"],
        "preferred_skills": ["Jetpack Compose", "ExoPlayer", "MVVM"],
        "location": "Noida, India",
        "stipend": "₹35,000/month",
        "description": "Build features for PW's Android app serving 30M+ students preparing for competitive exams. Work on live classes, doubt solving, and practice tests.",
        "apply_link": "https://pw.live/careers"
    },
    # --- HealthTech ---
    {
        "company": "1mg (Tata Health)",
        "role": "Backend Developer Intern",
        "required_skills": ["Python", "Django", "PostgreSQL", "REST APIs"],
        "preferred_skills": ["Celery", "Redis", "Docker"],
        "location": "Gurugram, India",
        "stipend": "₹55,000/month",
        "description": "Build APIs for India's leading digital healthcare platform. Work on medicine delivery, lab tests, doctor consultations, and health records.",
        "apply_link": "https://www.1mg.com/careers"
    },
    {
        "company": "Practo",
        "role": "Full Stack Intern",
        "required_skills": ["React", "Python", "PostgreSQL", "REST APIs"],
        "preferred_skills": ["Django", "TypeScript", "Docker"],
        "location": "Bangalore, India",
        "stipend": "₹50,000/month",
        "description": "Build healthcare software used by 20M patients and 300K doctors. Work on appointment booking, EHR systems, and telemedicine features.",
        "apply_link": "https://practo.com/careers"
    },
    # --- Logistics / Supply Chain ---
    {
        "company": "Delhivery",
        "role": "Software Engineering Intern",
        "required_skills": ["Python", "PostgreSQL", "REST APIs", "Algorithms"],
        "preferred_skills": ["Go", "Kafka", "Redis", "GIS"],
        "location": "Gurugram, India",
        "stipend": "₹60,000/month",
        "description": "Build route optimization, tracking, and warehouse management systems for India's largest fully-integrated logistics company.",
        "apply_link": "https://www.delhivery.com/careers"
    },
    {
        "company": "Dunzo",
        "role": "Backend Intern",
        "required_skills": ["Python", "FastAPI", "PostgreSQL", "Docker"],
        "preferred_skills": ["Redis", "Kafka", "Kubernetes", "GIS"],
        "location": "Bangalore, India",
        "stipend": "₹45,000/month",
        "description": "Build real-time delivery orchestration systems handling route optimization, partner management, and order fulfillment.",
        "apply_link": "https://www.dunzo.com/careers"
    },
    # --- HR Tech ---
    {
        "company": "Darwinbox",
        "role": "Full Stack Intern",
        "required_skills": ["React", "Node.js", "MongoDB", "REST APIs"],
        "preferred_skills": ["TypeScript", "GraphQL", "Docker"],
        "location": "Hyderabad, India",
        "stipend": "₹50,000/month",
        "description": "Build HR software features like payroll, performance management, and employee engagement tools used by 850+ enterprises.",
        "apply_link": "https://darwinbox.com/careers"
    },
    {
        "company": "Keka HR",
        "role": "Backend Developer Intern",
        "required_skills": ["C#", ".NET", "SQL Server", "REST APIs"],
        "preferred_skills": ["Azure", "React", "TypeScript"],
        "location": "Hyderabad, India",
        "stipend": "₹40,000/month",
        "description": "Build modern HR and payroll software features for Keka's platform used by 8000+ businesses to manage their workforce.",
        "apply_link": "https://www.keka.com/careers"
    },
    # --- AgriTech ---
    {
        "company": "DeHaat",
        "role": "Software Engineering Intern",
        "required_skills": ["Python", "Django", "PostgreSQL", "REST APIs"],
        "preferred_skills": ["Machine Learning", "GIS", "Mobile Development"],
        "location": "Patna, India",
        "stipend": "₹35,000/month",
        "description": "Build digital solutions for India's 140M farmers. Work on crop advisory, input delivery, and market linkage platforms.",
        "apply_link": "https://dehaat.com/careers"
    },
    # --- Consulting / IT Services ---
    {
        "company": "Wipro",
        "role": "Project Engineering Intern",
        "required_skills": ["Java", "SQL", "REST APIs", "Git"],
        "preferred_skills": ["Spring Boot", "AWS", "Testing"],
        "location": "Multiple Locations, India",
        "stipend": "₹25,000/month",
        "description": "Work on enterprise application development, testing, and delivery for Wipro's global clients across BFSI, healthcare, and manufacturing.",
        "apply_link": "https://careers.wipro.com/careers-home/"
    },
    {
        "company": "HCLTech",
        "role": "Software Trainee Intern",
        "required_skills": ["Java", "SQL", "Python", "Git"],
        "preferred_skills": ["AWS", "Docker", "Agile", "JIRA"],
        "location": "Noida, India",
        "stipend": "₹20,000/month",
        "description": "Develop software solutions for HCL's global enterprise clients. Gain exposure to the full software development lifecycle in an enterprise environment.",
        "apply_link": "https://www.hcltech.com/careers"
    },
]


def seed():
    print(f"Seeding {len(INTERNSHIPS)} internship records...")
    
    # Delete existing records
    supabase.table("internships").delete().neq("id", 0).execute()
    print("Cleared existing records.")
    
    # Insert all records
    result = supabase.table("internships").insert(INTERNSHIPS).execute()
    print(f"Successfully inserted {len(result.data)} internship records.")
    return result.data


if __name__ == "__main__":
    seed()
