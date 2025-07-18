1)How the system works:

    The user should input a research question, and the AI will present below items:

        a) A list of referenced sources (with URLs and titles)

        b) Bullet-point summaries from each source

        c) A final research report based on all findings in b) in plain language

2)Which API keys are required?

    a) Gemini
    
    b) Tavily

3)How to set the API key in .env and secrets(streamlit):

    [.env case] In code editor, create a .env file, enter GEMINI_API_KEY = "enter_your_original_api_key_here" without " "
    
    [secrets case] In code editor, create a secrets.toml file, enter GEMINI_API_KEY = "enter_your_original_api_key_here" or in streamlit app, go to SECRETS tab and insert GEMINI_API_KEY = "enter_your_original_api_key_here"

4)Sample input/output for each plan type:

sample user input:

    impact of ai on mental health?

sample system ouput:

    📚 Gathered Sources

        1. The Impact of AI in the Mental Health Field | Psychology Today
        https://www.psychologytoday.com/us/blog/invisible-bruises/202407/the-impact-of-ai-in-the-mental-health-field

        2. The mental health implications of artificial intelligence adoption
        https://www.nature.com/articles/s41599-024-04018-w

        3. The Potential Influence of AI on Population Mental Health - PMC
        https://pmc.ncbi.nlm.nih.gov/articles/PMC10690520/

        4. AI Can Positively Impact Mental Health - School of Social Work
        https://socialwork.uconn.edu/2024/02/27/ai-can-positively-impact-mental-health/

        5. Enhancing mental health with Artificial Intelligence: Current trends ...
        https://www.sciencedirect.com/science/article/pii/S2949916X24000525


    📝 Source-wise Summaries

        The Impact of AI in the Mental Health Field | Psychology Today

            AI shows promise in detecting medical and mental health conditions such as Autism and seizures.
        
        The mental health implications of artificial intelligence adoption

            Rapid AI adoption in organizations presents both opportunities and challenges for employees.
            Future research is needed to explore factors influencing the relationship between AI adoption, job stress, burnout, and self-efficacy in diverse contexts.
            Few empirical studies have specifically examined how AI adoption affects employees' mental health, particularly burnout, despite extensive research on its practical deployment.

        The Potential Influence of AI on Population Mental Health - PMC

            AI may influence population mental health through three main avenues: Advancing mental health care. Altering social and economic contexts. Shaping policies for the adoption, use, and potential misuse of AI-enhanced tools.
                
        AI Can Positively Impact Mental Health - School of Social Work

            AI can help individuals become more aware of mental health needs and encourage them to seek professional help.
            It can reduce social stigma through the use of virtual mental health therapists (e.g., BetterHelp, Talkspace) and chatbots.
            ChatGPT can be utilized in psychotherapy to create templates, allow for clinical personalization, and reduce cognitive load and documentation time.

        Enhancing mental health with Artificial Intelligence: Current trends ...

            This content outlines criteria for including papers on AI in mental healthcare, specifically:
            Papers published in peer-reviewed journals, conference proceedings, or reputable online databases.
            Papers specifically focusing on AI applications in mental healthcare.
            Review papers offering comprehensive overviews, analyses, or integration of existing English-language literature.
            It highlights the importance of addressing bias in big data and AI for healthcare, as well as algorithmic bias contributing to health inequities.

        
    📄 Final Research Report

        AI's Evolving Role in Mental Health: Opportunities and Challenges
            Artificial Intelligence (AI) is rapidly integrating into various aspects of life, presenting a multifaceted impact on mental health. This report synthesizes current findings regarding AI's potential benefits, emerging challenges, and critical areas for future consideration in this field.

        Advancing Mental Healthcare

            AI holds significant promise in enhancing mental health services and outcomes. Key applications include:

            Early Detection: AI demonstrates potential in detecting mental and medical conditions such as Autism and seizures, allowing for earlier intervention.

            Increased Awareness & Access: AI tools can help individuals become more aware of their mental health needs and encourage them to seek professional help. Virtual mental health therapists (e.g., BetterHelp, Talkspace) and chatbots can also reduce social stigma associated with seeking care.

            Therapeutic Support: AI can assist psychotherapists by generating templates, enabling clinical personalization, and reducing cognitive load and documentation time, thereby streamlining workflows.

            Population-Level Influence: Beyond direct care, AI can advance overall population mental health by improving care delivery, altering social and economic contexts, and informing policies for the responsible adoption and use of AI-enhanced tools.

        Workplace and Societal Implications
            
            While offering opportunities, the rapid adoption of AI also introduces notable challenges:

            Employee Well-being: The swift integration of AI into organizations can present both benefits and risks for employee mental health. Concerns exist regarding potential increases in job stress and burnout, though empirical studies specifically examining AI adoption's impact on employee mental health are still limited.

            Broader Contextual Shifts: AI's influence on population mental health extends to its capacity to reshape social and economic landscapes, which in turn can impact mental well-being. Furthermore, policy decisions regarding AI's deployment and potential misuse will be crucial in shaping its overall mental health implications.

        Addressing Bias and Research Needs

            To ensure AI's beneficial integration into mental healthcare, critical considerations and research gaps must be addressed:

            Algorithmic Bias: It is paramount to address inherent biases in big data and AI algorithms, as these can contribute to health inequities if left unmitigated.

            Understanding Impacts: Future research is essential to thoroughly explore the factors influencing the relationship between AI adoption, job stress, burnout, and self-efficacy in diverse professional and personal contexts.

            Empirical Evidence: There is a clear need for more empirical studies specifically investigating how AI adoption affects employees' mental health, particularly aspects like burnout.

            Research Standards: Robust research in this area requires adherence to criteria such as the inclusion of peer-reviewed literature focusing on AI applications in mental healthcare, and comprehensive review papers integrating existing knowledge.


        Conclusion

        AI presents a complex and evolving landscape for mental health. It offers innovative solutions for improved detection, access, and personalized care. However, its rapid integration into workplaces and society necessitates careful consideration of potential stressors, such as job-related anxiety and the ethical implications of algorithmic bias. To maximize AI's positive impact while mitigating risks, continued rigorous research and thoughtful policy development are crucial to guide its responsible and equitable application in promoting mental well-being.