# title-verification-system
Project Overview :

The Title Verification System is an AI-powered online platform designed to automatically verify new title submissions by comparing them against existing titles maintained by the Press Registrar General of India (PRGI). The system ensures that each submitted title is unique, compliant with guidelines, and does not create confusion with existing publications.

The system addresses real-world challenges, such as:

*Detecting titles that are too similar to existing ones.
*Enforcing disallowed words, prefixes, and suffixes to maintain decorum and avoid sensitive terms.
*Preventing creation of titles by combining existing titles or modifying periodicity (daily, weekly, monthly).
*Providing a probability score indicating the likelihood of a title being verified.
*By integrating rule-based validation and AI-powered semantic similarity, the system can handle both simple variations (spelling mistakes, prefixes/suffixes) and complex semantic similarities, including cross-lingual equivalence.

Objectives :

*Automatically detect similar or duplicate titles from a large database (~160,000 existing titles).
*Enforce PRGI guidelines regarding disallowed words, prefixes, suffixes, and periodicity.
*Provide clear user feedback and a verification probability score.
*Support scalable performance for handling multiple title submissions efficiently.

Key Features : 

*Rule-based checks for disallowed words and title combinations.
*String similarity detection using Levenshtein distance or fuzzy matching.
*AI-based semantic similarity detection (planned integration with Sentence-BERT).
*User-friendly feedback with reasons for rejection and probability scores.
*Modular and scalable design for future improvements.
