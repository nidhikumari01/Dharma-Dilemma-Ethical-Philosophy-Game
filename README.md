# 🧠 Dharma Dilemma: Ethical Philosophy Game

> “What would Krishna do? What would Kant say? Your choices define your Dharma.”

**Dharma Dilemma** is an interactive, AI-powered web game that presents you with moral and ethical dilemmas. You choose how to act — and receive feedback from great philosophical minds like **Immanuel Kant**, **Lord Krishna**, **Nietzsche**, and others. Learn ethical reasoning, explore philosophy, and reflect on your decisions.

---

## 🎯 Purpose

In an age of complex decisions, this project helps users:
- Explore personal ethics through action
- Understand moral frameworks (duty, consequence, virtue, dharma)
- See how ancient and modern thinkers might interpret tough choices

Perfect for students, philosophy lovers, and curious minds alike.

---

## 🕹️ How It Works

1. **Scenario Appears**  
   You’re presented with a real-world ethical dilemma.
   
2. **Make a Choice**  
   Choose between two actions — both challenging in their own way.

3. **Get AI-Powered Feedback**  
   The app generates responses inspired by famous philosophers, explaining how each might interpret your decision.

4. **Reflect and Learn**  
   Engage with ideas from deontology, utilitarianism, dharma, stoicism, and more.

---

## 🧪 Example Scenario

**Scenario:**  
> Your sibling committed a crime. You're the only witness.

**Choices:**
- A: Stay silent to protect your sibling  
- B: Report to authorities  

**Philosopher Feedback:**
- **Kant:** "You acted with moral duty; truth is non-negotiable."
- **Krishna:** "Let action be aligned with dharma, without attachment to outcomes."
- **Nietzsche:** "Did you obey rules, or create your own values?"

---

## 🧱 Tech Stack

| Tech            | Description                                  |
|-----------------|----------------------------------------------|
| `Streamlit`     | UI framework for building the game frontend  |
| `Groq API`      | Access to ultra-fast LLaMA 3 models          |
| `Python`        | Core game logic                              |
| `dotenv`        | Secure environment variable loading          |
| `OpenAI SDK`    | Used with Groq-compatible base URL           |

---

## API Integration
We're using Groq's hosted LLaMA 3 models via the OpenAI-compatible SDK.
To query them:

openai.api_key = os.getenv("GROQ_API_KEY")
openai.base_url = "https://api.groq.com/openai/v1/chat/completions"

## Supported models include:

1. llama3-8b-8192

2. llama3-70b-8192

3. mixtral-8x7b-32768

4. gemma-7b-it

## 🔮 Future Features
🧑‍🤝‍🧑 Multiplayer dilemma debates

🪙 Scoring based on philosophical alignment

✍️ User-submitted dilemmas & community voting

📈 Analytics dashboard for reflection patterns

🌐 Multilingual support (e.g., Hindi, Latin, Tamil)

## Live Demo
Coming soon at dharma-dilemma.vercel.app (or Streamlit Cloud).

## 🙏 Acknowledgments
Inspired by the Bhagavad Gita, Western moral philosophy, and your everyday life choices.

Powered by Groq and Streamlit for blazing-fast, accessible design.


