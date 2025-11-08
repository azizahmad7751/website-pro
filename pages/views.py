from django.shortcuts import render

def home(request):
    services = [
        {"title":"Web Development","desc":"Django/HTMX, React, high-performance builds.","icon":"💻"},
        {"title":"UI/UX & Brand","desc":"Design systems, identity, prototypes.","icon":"🎨"},
        {"title":"Automation","desc":"Workflows, internal tools, integrations.","icon":"⚙️"},
        {"title":"Apps & APIs","desc":"Scalable backends and REST APIs.","icon":"🧩"},
        {"title":"Security","desc":"Audits, hardening, best practices.","icon":"🔐"},
        {"title":"Launch & Growth","desc":"SEO, analytics, a/b testing.","icon":"🚀"},
    ]
    testimonials = [
        {"name":"Ava Thompson","role":"COO, Acme","quote":"They shipped on time with outstanding quality. Our KPIs jumped in weeks."},
        {"name":"Liam Patel","role":"Founder, FlowPay","quote":"Reliable, proactive, and senior across the stack. Highly recommended."}
    ]
    stats = [
        {"label":"Projects delivered","value":"120+"},
        {"label":"Avg. Lighthouse","value":"98/100"},
        {"label":"Client NPS","value":"72"},
        {"label":"Response time","value":"< 24h"},
    ]
    logos = ["logo.svg","logo.svg","logo.svg","logo.svg"]
    return render(request, "pages/home.html", {"services": services, "testimonials": testimonials, "stats": stats, "logos": logos})

def services(request):
    items = [
        {"title":"Strategy","points":["Discovery workshops","Architecture & security","Delivery plan"]},
        {"title":"Design","points":["Brand identity","Design systems","Responsive UI/UX"]},
        {"title":"Development","points":["Django/HTMX","REST APIs","Postgres & auth","CI/CD pipelines"]},
        {"title":"Growth","points":["Analytics & SEO","Performance & a11y","A/B testing"]},
    ]
    process = [
        {"step":"01","title":"Discover","desc":"Understand goals, users, and constraints."},
        {"step":"02","title":"Design","desc":"Wireframes, prototypes, design system."},
        {"step":"03","title":"Build","desc":"Sprints with demos and feedback."},
        {"step":"04","title":"Launch","desc":"Staging, QA, deploy, measure."},
    ]
    return render(request, "pages/services.html", {"items": items, "process": process})

def about(request):
    return render(request, "pages/about.html")
