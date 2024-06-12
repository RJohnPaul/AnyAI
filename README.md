# AnyAI 🚀🤖

![](https://github.com/RJohnPaul/AnyAI/blob/c7408f4ee18326098ed85602ee374c77bfce59c4/2560x1600%20(8).png)

AnyAI is a versatile AI tool that integrates Google Gemini and Google Vision APIs to provide powerful content generation and image classification capabilities. This repository contains the source code for the AnyAI web application built using Streamlit.

## Features

### AI Content Generator
Using the Google Gemini API, AnyAI can generate content for various platforms, including:
- LinkedIn Posts
- Blog Posts
- Instagram Posts
- Tweets
- Product Descriptions
- Emails
- Ad Copies
- Taglines
- Video Scripts
- Podcast Scripts
- SEO Content
- README Files
- Documentation
- Presentations
- Social Media Posts
- Articles

### Image Classifier
Using the Google Vision API, AnyAI can classify images either via upload or URL based on the entered query.

## Getting Started

### Prerequisites
- Python 3.7+
- Streamlit
- Pandas
- Google API credentials

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/AnyAI.git
   cd AnyAI
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API credentials. Create an `.env` file in the project root and add your API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

### Running the Application

To run the application, execute the following command in your terminal:
```bash
streamlit run app.py
```

This will start a local server and open the web application in your default web browser.

## Usage

1. **Visit Google AI Studio:**
   Go to [Google AI Studio](https://ai.google.dev/).

2. **Get API Key:**
   Click on "Get API Key" and create your API key.

3. **Copy API Key:**
   Copy the generated API key.

4. **Paste in Web Application:**
   In your web application, there should be an input field to paste your API key. Paste the copied API key into this field.

5. **Generate Content and Classify Images:**
   Once the API key is validated, you can use the Gemini API to generate text content and the Vision API to classify images within your web application.

## Gemini Model Capabilities

| Capability       | Benchmark                                               | Higher is better | Description                |
|------------------|---------------------------------------------------------|------------------|----------------------------|
| MMLU             | Representation of questions in 57 subjects              | 90.0             | CoT@32*                    |
| CoT@32*          | Reasoning                                               | 86.4             | 5-shot** (reported)        |
| Big-Bench Hard   | Reading comprehension (F1 Score)                        | 83.6             | 3-shot                     |
| DROP             | Commonsense reasoning for everyday tasks                | 82.4             | Variable shots             |
| HellaSwag        | Basic arithmetic manipulations                          | 87.8             | 10-shot*                   |
| GSM8K            | Basic arithmetic manipulations                          | 94.4             | maj1@32                    |
| maj1@32          | Python code generation                                  | 92.0             | 5-shot CoT (reported)      |
| MATH             | Challenging math problems                               | 53.2             | 4-shot                     |
| HumanEval        | Python code generation                                  | 74.4             | 0-shot (IT)*               |
| Natural2Code     | Python code generation                                  | 74.9             | 0-shot                     |

## Learn More

For a deeper understanding and additional insights, check out the accompanying [blog post](https://deepmind.google/technologies/gemini/#introduction) dedicated to Google's Gemini Model. Let's embark on this exciting journey together! 🌟🔍

## Contributing

We welcome contributions to AnyAI! Please read our [CONTRIBUTING](CONTRIBUTING.md) guide for more information on how to contribute.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Google Gemini](https://ai.google.dev/)
- [Google Vision](https://cloud.google.com/vision)
- [Streamlit](https://streamlit.io/)

---

Made with ❤️ by [John Paul](https://github.com/RJohnPaul)
