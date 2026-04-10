# LANGUAGE DETECTION NLP (Complete Version)
# Install libraries if not available
try:
    from langdetect import detect, detect_langs, DetectorFactory
except:
    import os
    os.system("pip install langdetect")
    from langdetect import detect, detect_langs, DetectorFactory
# Set seed for reproducibility
DetectorFactory.seed = 0
# Language codes dictionary
LANGUAGE_CODES = {
    'en': 'English', 'te': 'Telugu', 'fr': 'French', 'hi': 'Hindi',
    'no': 'Norwegian', 'cs': 'Czech'
}
# Function to detect language
def detect_language(text):
    try:
        # Handle very short text
        if len(text.split()) < 3:
            return "en", "English", []
        # Detect language
        language_code = detect(text)
        language_name = LANGUAGE_CODES.get(language_code, "Unknown")
        # Get probability distribution
        probabilities = detect_langs(text)
        return language_code, language_name, probabilities
    except:
        return "en", "English", []
# Interactive input loop
while True:
    text = input("\nEnter text to detect language (or type 'exit' to stop): ")
    if text.lower() == "exit":
        print("Goodbye!")
        break
    code, name, probs = detect_language(text)
    print(f"Detected Language: {name} ({code})")
    print("Probabilities:", probs)
    print("-" * 50)
