# build_t4_rw1.py
# Generates 27 Reading & Writing Module 1 questions for Test 4

DOMAINS = {
    "CRAFT": "Craft and Structure",
    "INFO": "Information and Ideas",
    "CONV": "Standard English Conventions",
    "EXPR": "Expression of Ideas"
}

RW_TARGETS = ['D', 'B', 'A', 'C', 'B', 'D', 'C', 'A', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'A', 'B', 'D', 'C', 'B', 'A', 'C', 'D', 'C', 'A', 'B']

def make_hard_mcq(qid, domain, subdomain, diff, stimulus, prompt, correct_text, distractors, target_letter, explanation):
    target_idx = ord(target_letter) - ord('A')
    choices_texts = list(distractors[:3])
    choices_texts.insert(target_idx, correct_text)
    choices = [{"letter": chr(65 + i), "text": t} for i, t in enumerate(choices_texts)]
    full_explanation = f"Choice {target_letter} is correct. {explanation}"
    return {
        "id": qid,
        "type": "mcq",
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": diff,
        "stimulus": stimulus,
        "prompt": prompt,
        "choices": choices,
        "correctAnswer": target_letter,
        "explanation": full_explanation
    }

def get_rw_m1_questions():
    specs = [
        # Q1: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Medium",
         "The critic noted that while the director's early features were marked by an austere visual minimalism, her latest cinematic offering reveals a distinctly _____ aesthetic, replete with opulent set design, saturated Technicolor hues, and hyper-dense audio mixing.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "baroque",
         ["spartan", "somber", "utilitarian"],
         "The context contrasts the director's earlier 'austere visual minimalism' with her new style featuring 'opulent set design' and dense sensory saturation. 'Baroque' means elaborately ornamented or complex, perfectly contrasting with austere minimalism."),

        # Q2: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "Although the archival documents concerning the treaty were thought to have been completely destroyed during the 1944 bombardment, the diplomatic historian's discovery of a private cache in Zurich proved that the historical record was far from _____.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "irretrievable",
         ["unassailable", "provisional", "corroborated"],
         "The discovery of private records in Zurich showed that the historical record could still be recovered, meaning it was not 'irretrievable' (impossible to recover or regain)."),

        # Q3: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "Far from being _____ by the vehement condemnation from the established academic orthodoxy, Dr. Aris actively courted intellectual controversy, regarding vigorous debate as the sole authentic crucible of genuine philosophical breakthrough.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "intimidated",
         ["galvanized", "invigorated", "validated"],
         "The sentence states that 'Far from being _____, Dr. Aris actively courted controversy'. Thus the blank needs a word meaning daunted or deterred; 'intimidated' matches this contrast perfectly."),

        # Q4: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "In her treatise on algorithmic governance, sociologist Elena Rostova argues that machine-learning classifiers cannot be considered neutral arbiters; rather, their training sets inevitably _____ the latent socio-economic prejudices of the societies that compile them.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "perpetuate",
         ["vitiate", "circumscribe", "preclude"],
         "The sentence argues that algorithms are not neutral and that their training data continues or carries forward societal biases. 'Perpetuate' means to cause to continue indefinitely, matching the author's critique."),

        # Q5: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "The evolutionary biologist underscored that sexual dimorphism in avian plumage is rarely an arbitrary developmental accident; instead, it typically represents an intricately calibrated balance between sexual selection favoring conspicuousness and predatory pressure demanding _____.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "camouflage",
         ["fecundity", "hypertrophy", "magnificence"],
         "The text contrasts 'sexual selection favoring conspicuousness' (high visibility) with 'predatory pressure demanding' the opposite trait to avoid predation. 'Camouflage' (cryptic coloration/inconspicuousness) is the exact biological counterweight."),

        # Q6: Craft / Text Structure
        (DOMAINS["CRAFT"], "Text Structure and Purpose", "Hard",
         "In traditional historical scholarship, the 17th-century 'Scientific Revolution' was long canonized as a sudden, radical epistemic rupture spearheaded by a handful of European polymaths. Recent revisionist historiography, however, presents a decidedly more nuanced topography: by examining laboratory accounting ledgers, artisanal glassblowing workshops, and translated Ottoman astronomical manuscripts, contemporary scholars argue that empirical science was an accretive, global, and socio-technological phenomenon rather than an isolated intellectual epiphany.",
         "Which choice best describes the overall structure of the text?",
         "It outlines a longstanding academic paradigm and then delineates how recent empirical scholarship has substantially revised it.",
         ["It praises the methodological rigor of classical historiography before critiquing modern revisionism.",
          "It juxtaposes two equally flawed historical theories and proposes a third synthesis.",
          "It details the specific biographical contributions of European polymaths before questioning their integrity."],
         "The passage begins by describing the traditional canonical view of the Scientific Revolution and then explains how recent revisionist scholarship has modified and expanded that view through new socio-technological evidence."),

        # Q7: Dual Text / Cross-Text Connections
        (DOMAINS["CRAFT"], "Cross-Text Connections", "Hard",
         "Text 1\nClassical economic theory posits that market participants behave as rational utility maximizers possessed of coherent, stable preferences. Under this framework, anomalies in pricing or portfolio management are treated as transient friction rather than foundational defects of the rational-actor paradigm.\n\nText 2\nBehavioral economists have systematically demonstrated that cognitive heuristics, such as loss aversion and hyperbolic discounting, induce predictable, systemic irrationalities in financial decision-making. Far from being trivial edge cases, these psychological biases frequently generate persistent asset bubbles and structural market failures that classical models cannot anticipate.",
         "Based on the texts, how would the author of Text 2 most likely respond to the characterization of anomalies in Text 1?",
         "By asserting that pricing distortions reflect fundamental psychological architecture rather than negligible, self-correcting market friction.",
         ["By agreeing that human market behavior converges toward rational equilibrium over extended intervals.",
          "By contending that classical models overemphasize psychology at the expense of empirical fiscal policy.",
          "By claiming that systemic market failures can be entirely eradicated through improved algorithmic trading."],
         "Text 1 treats anomalies as 'transient friction', while Text 2 asserts that these distortions are 'predictable, systemic irrationalities' rooted in cognitive heuristics that create persistent failures."),

        # Q8: Central Ideas
        (DOMAINS["INFO"], "Central Ideas and Details", "Hard",
         "The linguistic anthropologist Edward Sapir observed that human beings do not live in the objective world alone, nor alone in the world of social activity as ordinarily understood, but are very much at the mercy of the particular language which has become the medium of expression for their society. To regard language as merely an incidental tool for solving specific problems of communication is an illusion. In reality, the 'real world' is to a large extent unconsciously built up on the language habits of the group, predetermining how individuals categorize, evaluate, and interpret their sensory reality.",
         "Which choice best states the primary claim of the passage?",
         "Language fundamentally shapes and structures the conceptual reality through which humans perceive and interpret the world.",
         ["Human cognition is entirely decoupled from lexical structures and communicative conventions.",
          "Objective reality can be faithfully perceived only when individuals master multiple disparate linguistic traditions.",
          "Language evolved exclusively as a pragmatic instrument for coordinating communal hunting and trade activities."],
         "The passage emphasizes that language is not merely a tool for communication, but actively builds and predetermines how humans categorize and perceive reality."),

        # Q9: Inferences
        (DOMAINS["INFO"], "Inferences", "Hard",
         "Paleoclimatologists analyzing high-resolution ice cores extracted from the Greenland ice sheet observed that during the Dansgaard-Oeschger events of the last glacial period, local temperatures surged by as much as 10 degrees Celsius within a few decades. Such abrupt warming coincided with rapid shifts in the Atlantic Meridional Overturning Circulation (AMOC). Because contemporary climate models project significant weakening of AMOC under severe anthropogenic greenhouse forcing, many oceanographers express apprehension that _____.",
         "Which choice most logically completes the text?",
         "the modern climate system may possess non-linear thresholds that could trigger abrupt and severe regional climatic instability.",
         ["future global temperatures will stabilize indefinitely once greenhouse gas concentrations peak.",
          "paleoclimatic models from the last glacial period have no methodological relevance to modern atmospheric mechanics.",
          "the Greenland ice sheet will completely expand southward into temperate oceanic latitudes."],
         "The text explains that past rapid warmings were tied to AMOC shifts, and since AMOC may weaken today, oceanographers worry that abrupt, non-linear climatic shifts could occur in our modern system."),

        # Q10: Command of Evidence (Textual)
        (DOMAINS["INFO"], "Command of Evidence", "Hard",
         "In their 2023 study of mycorrhizal networks in temperate deciduous forests, ecologist Dr. Hiroshi Tanaka and colleagues investigated whether mature 'hub trees' actively direct carbon resources preferentially to conspecific (same-species) seedlings over heterospecific (different-species) seedlings under severe drought conditions. Tanaka hypothesized that resource transfer through common mycelial networks is mediated by evolutionary kin recognition rather than indiscriminate passive diffusion across a concentration gradient.",
         "Which finding, if true, would most directly support Tanaka's hypothesis?",
         "Isotope-labeled carbon injected into mature oak trees appeared in significantly higher concentrations in drought-stressed oak saplings than in neighboring beech saplings located at an equivalent distance.",
         ["Carbon transfer between mature trees and seedlings ceased altogether whenever soil moisture dropped below baseline thresholds.",
          "Seedlings of all species exhibited equal rates of carbon uptake when mycorrhizal hyphae were severed by mechanical trenching.",
          "Mature beech trees absorbed carbon from neighboring oak seedlings under conditions of ample rainfall."],
         "To support kin recognition over passive diffusion, carbon must flow preferentially to same-species (conspecific) seedlings over different-species seedlings at the same distance."),

        # Q11: Command of Evidence (Quantitative / Logic)
        (DOMAINS["INFO"], "Command of Evidence", "Hard",
         "A team of behavioral neuroscientists studied cognitive flexibility in two cohorts of corvids: New Caledonian crows and Eurasian jays. In a multi-stage puzzle box requiring tools of three distinct lengths, New Caledonian crows succeeded on their initial trial in 82% of instances, whereas Eurasian jays succeeded in 38% of instances. However, when the sequential order of physical barriers inside the puzzle box was inverted without warning, the New Caledonian crows took an average of 14 trials to abandon their previously learned sequence, whereas Eurasian jays adapted to the new sequence in an average of 4 trials.",
         "Which choice is best supported by the experimental data?",
         "While New Caledonian crows demonstrated superior initial tool-use proficiency, Eurasian jays exhibited greater behavioral plasticity when confronted with unexpected procedural changes.",
         ["New Caledonian crows are biologically incapable of adapting to structural alterations in environmental problem-solving.",
          "Eurasian jays rely exclusively on trial-and-error mechanics rather than spatial reasoning during tool manipulation tasks.",
          "Inverting puzzle box barriers improved the performance speed of both corvid species equally."],
         "New Caledonian crows had higher initial success (82% vs 38%), but jays adapted much faster to inverted rules (4 trials vs 14 trials), showing greater flexibility/plasticity."),

        # Q12: Inferences / Logic Completion
        (DOMAINS["INFO"], "Inferences", "Hard",
         "When early twentieth-century physicists measured the photoelectric effect, classical electromagnetic wave theory predicted that increasing the intensity of incident light would elevate the kinetic energy of emitted photoelectrons. Yet experimental results repeatedly falsified this: the maximum kinetic energy depended solely on the frequency of the radiation, while intensity governed only the number of electrons emitted per second. Albert Einstein resolved this paradox by postulating that light propagates and interacts in discrete quanta (photons). Therefore, if incident light falls below the material's specific threshold frequency, _____.",
         "Which choice most logically completes the text?",
         "no electrons will be ejected from the metal regardless of how intensely the light beam illuminates the surface.",
         ["electrons will be ejected with kinetic energy directly proportional to the total exposure time.",
          "the emitted photoelectrons will travel faster than the speed of light in a vacuum.",
          "the metal will absorb the light energy and instantly emit high-energy gamma rays."],
         "Under Einstein's photon model, each individual photon must have energy E = hf exceeding the work function; if frequency is below the threshold, no single photon can eject an electron, regardless of beam intensity."),

        # Q13: Standard English Conventions (Punctuation / Clauses)
        (DOMAINS["CONV"], "Boundaries", "Medium",
         "During the excavation of the ancient Roman villa at Oplontis, archaeologists uncovered exquisite wall frescoes depicting theatrical masks, ornate architecture, and mythological _____ each rendered with sophisticated linear perspective and vibrant cinnabar pigments.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "creatures—",
         ["creatures", "creatures;", "creatures."],
         "The em-dash 'creatures—' appropriately sets off the concluding appositive clause/modifier elaborating on how each of the items in the series was rendered."),

        # Q14: Standard English Conventions (Subject-Verb Agreement)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "Neither the intricate navigational manuscripts recovered from the wrecked galleon nor the oral testimony provided by the surviving first _____ sufficient evidence to establish beyond doubt that the navigator deliberately altered the vessel's plotted heading.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "mate provides",
         ["mate provide", "mates provide", "mate were providing"],
         "Under the 'neither... nor...' construction with singular subjects joined by 'nor', the verb agrees with the closer subject ('the surviving first mate', singular), requiring the singular verb 'provides'."),

        # Q15: Standard English Conventions (Modifiers)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "Having spent nearly four decades painstakingly transcribing unpublished cuneiform tablets in the basement vaults of the British _____ Assyriologist Reginald Campbell Thompson finally deciphered the obscure epic fragments in 1928.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "Museum,",
         ["Museum, the", "Museum; the", "Museum and the"],
         "The introductory participial phrase 'Having spent nearly four decades...' modifies the subject who did the action, which must immediately follow the comma: 'Assyriologist Reginald Campbell Thompson'."),

        # Q16: Standard English Conventions (Semicolon vs Colon)
        (DOMAINS["CONV"], "Boundaries", "Hard",
         "The astrophysicist's radical hypothesis regarding dark matter relies upon a single foundational _____ namely, that weakly interacting massive particles interact not only gravitationally but also through a previously unobserved fifth fundamental force.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "premise:",
         ["premise;", "premise,", "premise"],
         "A colon is the appropriate mark of punctuation following an independent clause to introduce an explanation, clarification, or amplifying definition introduced by 'namely'."),

        # Q17: Standard English Conventions (Pronoun-Antecedent / Relative Clause)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "The international consortium of marine biologists published comprehensive genomic data on six newly cataloged deep-sea hydrothermal vent organisms, each of _____ unique metabolic enzymes capable of synthesizing ATP in the complete absence of solar radiation.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "which possesses",
         ["whom possess", "which possess", "them possessing"],
         "The relative pronoun 'which' refers to non-human organisms, and 'each of which' takes a singular verb: 'possesses'."),

        # Q18: Standard English Conventions (Verb Tense / Aspect)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "By the time the James Webb Space Telescope commenced its scientific operations in July 2022, astronomers around the world _____ for more than two decades for an instrument capable of resolving the cosmic dawn.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "had been waiting",
         ["have been waiting", "waited", "will have been waiting"],
         "The past perfect continuous ('had been waiting') correctly indicates an action that was ongoing in the past up until another past event ('commenced in July 2022')."),

        # Q19: Transitions
        (DOMAINS["EXPR"], "Transitions", "Medium",
         "In high-energy physics, the standard model successfully explains electromagnetic, weak, and strong nuclear interactions with remarkable mathematical precision. _____, it remains conspicuously incomplete, failing to incorporate general relativity or account for the existence of dark energy.",
         "Which choice completes the text with the most logical transition?",
         "Nevertheless,",
         ["Furthermore,", "Consequently,", "Similarly,"],
         "The second sentence contrasts the model's success with its conspicuous incompleteness. 'Nevertheless' provides the correct adversative transition."),

        # Q20: Transitions
        (DOMAINS["EXPR"], "Transitions", "Hard",
         "Many urban planners assumed that constructing high-capacity arterial highways would permanently alleviate severe suburban traffic congestion. _____, empirical traffic monitoring consistently demonstrates that expanding road capacity induces latent vehicular demand, ultimately returning commuter congestion to baseline levels within three years.",
         "Which choice completes the text with the most logical transition?",
         "In practice,",
         ["In addition,", "For example,", "Likewise,"],
         "The first sentence presents an assumption, while the second sentence presents what actually happens when roads are built. 'In practice' perfectly sets up the empirical reality contradicting the theoretical assumption."),

        # Q21: Transitions
        (DOMAINS["EXPR"], "Transitions", "Hard",
         "Dendrochronologists can determine the precise calendar year in which a historical timber structure was erected by cross-matching annual growth ring sequences against established regional master chronologies. _____, wood samples displaying fewer than thirty distinct growth rings typically lack sufficient statistical variance to achieve an unequivocal chronological match.",
         "Which choice completes the text with the most logical transition?",
         "However,",
         ["Indeed,", "Accordingly,", "Hence,"],
         "The first sentence notes what dendrochronologists can do, while the second states a critical limitation (samples with under 30 rings lack sufficient variance). 'However' is the appropriate contrastive transition."),

        # Q22: Rhetorical Synthesis
        (DOMAINS["EXPR"], "Rhetorical Synthesis", "Medium",
         "While researching a topic, a student has taken the following notes:\n- The Svalbard Global Seed Vault is a secure seed bank located on the Norwegian island of Spitsbergen.\n- It was established in 2008 to preserve crop diversity against catastrophic global loss.\n- The facility is excavated deep inside a sandstone mountain in an area with low tectonic activity and permanent permafrost.\n- Even in the event of total electrical power failure, the natural permafrost ensures that samples remain frozen for decades.\n- It currently safeguards over 1.2 million distinct agricultural seed samples from nearly every country.",
         "The student wants to explain how the physical location of the Svalbard facility ensures the long-term preservation of stored seeds. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
         "Excavated deep within a tectonically stable sandstone mountain in Spitsbergen, the Svalbard vault relies on natural permafrost to keep seeds frozen even during total electrical failure.",
         ["Established in 2008 on an island in Norway, the Svalbard Global Seed Vault currently preserves over 1.2 million distinct agricultural seed samples.",
          "The facility on Spitsbergen safeguards crop diversity against catastrophic global events using samples collected from nearly every country on Earth.",
          "Over 1.2 million seed accessions have been deposited in the Svalbard Global Seed Vault since its construction began deep within a mountain in 2008."],
         "Choice A specifically highlights the physical location (tectonically stable mountain in Spitsbergen, natural permafrost) and explains how it guarantees preservation without power."),

        # Q23: Rhetorical Synthesis
        (DOMAINS["EXPR"], "Rhetorical Synthesis", "Hard",
         "While researching a topic, a student has taken the following notes:\n- Radiocarbon dating measures the decay of carbon-14 in organic materials up to approximately 50,000 years old.\n- Potassium-argon (K-Ar) dating measures the radioactive decay of potassium-40 into argon-40 in volcanic rock.\n- Potassium-40 has a half-life of 1.25 billion years, making K-Ar dating effective for volcanic strata aged between 100,000 and 4.5 billion years old.\n- Early hominin fossils discovered in the East African Rift Valley are frequently found embedded between sedimentary layers of volcanic tuff.\n- Because hominin bones themselves contain almost no surviving collagen, paleoanthropologists date the fossils indirectly by dating the bounding volcanic tuff layers using potassium-argon analysis.",
         "The student wants to explain to an audience of archaeology students why potassium-argon dating is preferred over radiocarbon dating for East African hominin fossils. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
         "Because East African hominin fossils typically exceed radiocarbon dating's 50,000-year ceiling and lack collagen, researchers use potassium-argon dating on the surrounding volcanic tuff to establish ages that can span millions of years.",
         ["Radiocarbon dating measures the decay of carbon-14 in organic matter up to 50,000 years old, whereas potassium-argon dating measures volcanic rock decays.",
          "Paleoanthropologists in the East African Rift Valley analyze sedimentary layers of volcanic tuff that formed between 100,000 and 4.5 billion years ago.",
          "Potassium-40 decays into argon-40 with a half-life of 1.25 billion years, which enables geologists to date ancient volcanic rock with high precision."],
         "Choice A directly addresses the prompt by explaining why radiocarbon cannot be used (exceeds 50,000 years, bones lack collagen) and why K-Ar is used on surrounding volcanic tuff."),

        # Q24: Vocab / Tone
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "Rather than viewing the sudden collapse of the Bronze Age eastern Mediterranean palace economies as the result of a single cataclysmic invasion, modern archaeologists favor a systems-collapse model wherein multiple stressors—drought, trade disruption, and civil unrest—interacted to _____ the sociopolitical infrastructure.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "undermine",
         ["consolidate", "insulate", "vindicate"],
         "The stressors interacted to weaken or bring down the palace economies. 'Undermine' means to subvert or gradually weaken."),

        # Q25: Craft / Point of View / Tone
        (DOMAINS["CRAFT"], "Text Structure and Purpose", "Hard",
         "It is often asserted that the primary virtue of mathematical formalization in theoretical economics is the elimination of ambiguity. By translating intuitive concepts into rigorous symbolic notation, propositions can supposedly be evaluated with axiomatic clarity. Yet this formal elegance frequently conceals substantive epistemic hazards: mathematical models achieve deductive precision only by making radical simplifying abstractions that strip human behavior of the very messy institutional and psychological contingencies that govern real-world transactions.",
         "Which choice best describes the author's primary attitude toward mathematical formalization in economics?",
         "Skeptical of its claim to neutrality, cautioning that technical rigor often masks severe and unrealistic simplifications.",
         ["Wholly dismissive of mathematical logic, urging economists to abandon quantitative modeling entirely.",
          "Unreservedly enthusiastic about its capacity to replace flawed human intuition with axiomatic certainty.",
          "Indifferent to the methodological debate, viewing mathematical models and intuitive narratives as interchangeable."],
         "The author acknowledges the apparent virtue of formalization but cautions that it conceals substantive hazards through radical simplifying abstractions."),

        # Q26: Standard English Conventions (Coordination / Run-on prevention)
        (DOMAINS["CONV"], "Boundaries", "Hard",
         "The synthesis of carbon nanotubes requires extraordinarily precise thermal _____ even minor temperature deviations of two degrees Celsius can disrupt catalyst activation and produce disordered amorphous soot.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "regulation;",
         ["regulation", "regulation, so", "regulation, for"],
         "Two complete independent clauses must be joined with a semicolon (or comma + coordinating conjunction), making 'regulation;' grammatically sound."),

        # Q27: Inferences
        (DOMAINS["INFO"], "Inferences", "Hard",
         "In marine bioacoustics, the SOFAR (Sound Fixing and Ranging) channel is a horizontal oceanic layer where the speed of sound reaches a global minimum due to the opposing gradients of temperature and hydrostatic pressure. Because sound waves that refract back into this low-velocity duct cannot lose energy to surface waves or sea-floor bathymetry, low-frequency acoustic signals within the channel can propagate across thousands of kilometers with negligible attenuation. Consequently, marine biologists hypothesize that baleen whales communicating at low frequencies _____.",
         "Which choice most logically completes the text?",
         "may utilize the acoustic properties of the SOFAR channel to coordinate across entire ocean basins.",
         ["are unable to detect vocalizations from conspecifics situated more than a few nautical miles away.",
          "must swim to shallow coastal shelves in order to broadcast mating calls over long distances.",
          "suffer profound auditory trauma whenever they dive into deep oceanic low-velocity layers."],
         "Since low-frequency signals in the SOFAR channel travel thousands of kilometers without attenuation, baleen whales using low frequencies could utilize this to coordinate across vast ocean basins.")
    ]
    
    questions = []
    for i, spec in enumerate(specs):
        qid = f"t4-rw1-q{i+1}"
        domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        target_letter = RW_TARGETS[i]
        questions.append(make_hard_mcq(qid, domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))
    return questions
