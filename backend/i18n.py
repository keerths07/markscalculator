import streamlit as st

LANGUAGES = {
    "en": "English",
    "hi": "हिन्दी",
    "te": "తెలుగు",
}

TRANSLATIONS = {
    "en": {
        "home": "Home",
        "add_student": "Add Student",
        "home.title": "Home",
        "home.welcome": "Welcome to the Student Management System",
        "home.info": "Use the sidebar to manage students and marks",
        "home_features": (
            "This application allows you to:\n\n"
            "- Add Students\n"
            "- Enter Student Marks\n"
            "- View Student Results\n"
            "- Generate AI-powered performance insights"
        ),
        "local_ai": "Local AI Inference (Ollama)",
        "marks_saved": "Marks Saved Successfully!",
        "maths_marks": "Maths Marks",
        "model": "Model",
        "no_data": "No student or marks data found.",
        "ollama_model": "Ollama model",
        "ollama_url": "Ollama URL",
        "save_marks": "Save Marks",
        "science_marks": "Science Marks",
        "student_added": "Student Added Successfully!",
        "student_id": "Student ID",
        "student_name": "Student Name",
        "view_results": "View Results",
    },
    "hi": {
        "add_student": "छात्र जोड़ें",
        "add_student_button": "छात्र जोड़ें",
        "ai_base_url": "API बेस URL",
        "ai_insights": "AI सुझाव",
        "ai_provider": "AI प्रदाता",
        "api_credential": "API क्रेडेंशियल",
        "byok": "BYOK - अपना टोकन उपयोग करें",
        "english_marks": "अंग्रेज़ी अंक",
        "enter_api_credential": "BYOK उपयोग करने के लिए अपनी API जानकारी दर्ज करें।",
        "enter_marks": "अंक दर्ज करें",
        "generate_ai_insights": "AI सुझाव बनाएं",
        "generating_byok": "आपके टोकन से सुझाव बनाए जा रहे हैं...",
        "generating_local": "स्थानीय AI से सुझाव बनाए जा रहे हैं...",
        "home": "होम",
        "home_intro": "छात्र प्रबंधन प्रणाली में आपका स्वागत है",
        "home_features": (
            "यह एप्लिकेशन आपको ये काम करने देता है:\n\n"
            "- छात्र जोड़ें\n"
            "- छात्रों के अंक दर्ज करें\n"
            "- छात्रों के परिणाम देखें\n"
            "- AI-संचालित प्रदर्शन सुझाव बनाएं"
        ),
        "local_ai": "स्थानीय AI इंफरेंस (Ollama)",
        "marks_saved": "अंक सफलतापूर्वक सहेजे गए!",
        "maths_marks": "गणित अंक",
        "model": "मॉडल",
        "no_data": "छात्र या अंक डेटा नहीं मिला।",
        "ollama_model": "Ollama मॉडल",
        "ollama_url": "Ollama URL",
        "save_marks": "अंक सहेजें",
        "science_marks": "विज्ञान अंक",
        "student_added": "छात्र सफलतापूर्वक जोड़ा गया!",
        "student_id": "छात्र ID",
        "student_name": "छात्र का नाम",
        "view_results": "परिणाम देखें",
    },
    "te": {
        "add_student": "విద్యార్థిని చేర్చండి",
        "add_student_button": "విద్యార్థిని చేర్చండి",
        "ai_base_url": "API బేస్ URL",
        "ai_insights": "AI సూచనలు",
        "ai_provider": "AI ప్రొవైడర్",
        "api_credential": "API వివరాలు",
        "byok": "BYOK - మీ స్వంత టోకెన్ ఉపయోగించండి",
        "english_marks": "ఇంగ్లీష్ మార్కులు",
        "enter_api_credential": "BYOK ఉపయోగించడానికి మీ API వివరాలు నమోదు చేయండి.",
        "enter_marks": "మార్కులు నమోదు చేయండి",
        "generate_ai_insights": "AI సూచనలు రూపొందించండి",
        "generating_byok": "మీ టోకెన్‌తో సూచనలు రూపొందిస్తున్నాం...",
        "generating_local": "స్థానిక AIతో సూచనలు రూపొందిస్తున్నాం...",
        "home": "హోమ్",
        "home_intro": "విద్యార్థి నిర్వహణ వ్యవస్థకు స్వాగతం",
        "home_features": (
            "ఈ అప్లికేషన్‌లో మీరు చేయగలవి:\n\n"
            "- విద్యార్థులను చేర్చండి\n"
            "- విద్యార్థుల మార్కులు నమోదు చేయండి\n"
            "- విద్యార్థుల ఫలితాలు చూడండి\n"
            "- AI ఆధారిత పనితీరు సూచనలు రూపొందించండి"
        ),
        "local_ai": "స్థానిక AI ఇన్ఫరెన్స్ (Ollama)",
        "marks_saved": "మార్కులు విజయవంతంగా సేవ్ అయ్యాయి!",
        "maths_marks": "గణితం మార్కులు",
        "model": "మోడల్",
        "no_data": "విద్యార్థి లేదా మార్కుల డేటా కనిపించలేదు.",
        "ollama_model": "Ollama మోడల్",
        "ollama_url": "Ollama URL",
        "save_marks": "మార్కులు సేవ్ చేయండి",
        "science_marks": "సైన్స్ మార్కులు",
        "student_added": "విద్యార్థి విజయవంతంగా చేర్చబడింది!",
        "student_id": "విద్యార్థి ID",
        "student_name": "విద్యార్థి పేరు",
        "view_results": "ఫలితాలు చూడండి",
    },
}


def get_locale():
    if "locale" not in st.session_state:
        st.session_state.locale = "en"

    locales = list(LANGUAGES.keys())
    selected = st.sidebar.selectbox(
        "Language / भाषा / భాష",
        options=locales,
        format_func=lambda locale: LANGUAGES[locale],
        index=locales.index(st.session_state.locale),
        key="backend_locale_switcher",
    )
    st.session_state.locale = selected
    return selected


def translate(locale, key):
    return TRANSLATIONS.get(locale, TRANSLATIONS["en"]).get(key, key)


def language_name(locale):
    return LANGUAGES.get(locale, LANGUAGES["en"])