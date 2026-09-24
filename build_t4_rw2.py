# build_t4_rw2.py
# Generates 27 Reading & Writing Module 2 questions for Test 4 (100% Adaptive Hard Module)

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

def get_rw_m2_questions():
    specs = [
        # Q1: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "The political theorist's monograph was widely criticized by colleagues not for its methodological rigor, which was indisputable, but for its overtly _____ framing: every historical case study had been curated to validate the author's predetermined ideological conviction while omitting contradictory archival data.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "tendentious",
         ["dispassionate", "meticulous", "inchoate"],
         "The context explains that every case study was curated to advance a predetermined ideological conviction while omitting contradictory evidence. 'Tendentious' means expressing or intending to promote a particular cause or point of view, especially a biased one."),

        # Q2: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "Rather than operating as a _____ force within the delicate alpine tundra ecosystem, moderate seasonal grazing by native ungulates actually promotes biodiversity by suppressing aggressive perennial grasses that would otherwise choke out slow-growing endemic wildflowers.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "deleterious",
         ["salubrious", "regenerative", "negligible"],
         "The contrast 'Rather than operating as a _____ force... actually promotes biodiversity' requires a word meaning harmful or damaging. 'Deleterious' precisely fits this contrast."),

        # Q3: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "In realistic fiction, achieving authentic _____ requires far more than mere photographic cataloging of physical details; the author must also replicate the subtle cadences, hesitations, and psychological ambiguities of genuine human dialogue.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "verisimilitude",
         ["parsimony", "hyperbole", "anachronism"],
         "The passage discusses realistic fiction achieving an authentic appearance of truth or lifelikeness. 'Verisimilitude' means the appearance of being true or real."),

        # Q4: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "While popular accounts often describe the ancient philosopher's prose style as impenetrable and dry, literary historians note that his late dialogues contain remarkably _____ polemics that skewers contemporary political sophistry with razor-sharp irony.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "trenchant",
         ["soporific", "convoluted", "diffuse"],
         "The contrast is with 'impenetrable and dry'. His late dialogues contain polemics that skewer opponents with razor-sharp irony. 'Trenchant' means vigorous or incisive in expression or style, keen and sharp."),

        # Q5: Vocab
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "The pharmaceutical executive claimed that the clinical trial results provided definitive proof of efficacy, but bioethicists cautioned that drawing such sweeping conclusions from an unblinded study with a sample size of only twelve patients was entirely _____.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "unwarranted",
         ["irrefutable", "substantiated", "unassailable"],
         "Drawing sweeping conclusions from a tiny, unblinded study is completely unjustified or groundless. 'Unwarranted' fits the context perfectly."),

        # Q6: Craft / Text Structure
        (DOMAINS["CRAFT"], "Text Structure and Purpose", "Hard",
         "In his classic 1951 monograph, economist Kenneth Arrow formulated the 'Impossibility Theorem,' demonstrating mathematically that when voters have three or more distinct alternatives, no ranked-order electoral voting system can convert individual preferences into a community-wide ranking while simultaneously satisfying five basic axioms of fairness (such as non-dictatorship, Pareto efficiency, and independence of irrelevant alternatives). Arrow did not intend this proof as a cynical repudiation of democracy, but rather as an epistemic caution: collective decision-making inevitably involves ethical compromises among competing democratic ideals.",
         "Which choice best describes the primary function of the underlined portion (final sentence)?",
         "It clarifies the theoretical objective of a mathematical proof against potential misinterpretation.",
         ["It provides empirical counterexamples that invalidate Arrow's initial mathematical axioms.",
          "It urges political bodies to abandon democratic voting procedures in favor of technocratic appointments.",
          "It demonstrates that the five fairness axioms are mathematically redundant in multi-party systems."],
         "The last sentence ('Arrow did not intend this proof as a cynical repudiation... but rather as an epistemic caution...') clarifies the genuine intent and meaning of the theorem against misinterpretation."),

        # Q7: Dual Text / Cross-Text Connections
        (DOMAINS["CRAFT"], "Cross-Text Connections", "Hard",
         "Text 1\nEpigenetic modifications—such as DNA methylation and histone acetylation—alter gene expression without changing the underlying nucleotide sequence. Some developmental biologists have argued that transgenerational epigenetic inheritance represents a revival of Lamarckian evolution, demonstrating that environmentally acquired characteristics can be transmitted directly across multiple generations of offspring.\n\nText 2\nWhile transgenerational epigenetic inheritance has been definitively demonstrated in nematodes and plants, mammalian evidence remains exceptionally sparse. In mammals, the germline undergoes two comprehensive waves of genome-wide epigenetic reprogramming—first during gametogenesis and again immediately after fertilization. These erasure phases wipe clean virtually all ancestral chromatin marks, ensuring that Darwinian genetic selection, rather than soft Lamarckian inheritance, remains the primary engine of mammalian evolutionary adaptation.",
         "Based on Text 2, how would the author respond to the claim in Text 1 regarding Lamarckian evolution in mammals?",
         "With deep skepticism, citing the comprehensive biochemical erasure of epigenetic marks that takes place during mammalian germline development.",
         ["With enthusiastic agreement, noting that mammalian genomes are far more susceptible to methylation than plant genomes.",
          "By contending that DNA methylation alters underlying nucleotide sequences permanently in all vertebrate lineages.",
          "By arguing that nematodes and plants do not utilize histone modification mechanisms during reproduction."],
         "The author of Text 2 counters that in mammals, two waves of genome-wide epigenetic reprogramming 'wipe clean virtually all ancestral chromatin marks', rejecting Lamarckian claims for mammals."),

        # Q8: Central Ideas
        (DOMAINS["INFO"], "Central Ideas and Details", "Hard",
         "In celestial mechanics, the 'three-body problem' addresses the motion of three point-mass particles interacting under Newton's universal law of gravitation. In 1887, Henri Poincaré proved that, unlike the two-body problem which admits a closed-form analytic solution in terms of Keplerian orbits, the general three-body problem possesses no general algebraic solution and exhibits sensitive dependence on initial conditions. Poincaré's discovery demonstrated that determinism does not imply predictability: even in a purely deterministic Newtonian universe governed by precise differential equations, infinitesimal uncertainties in measurement can amplify exponentially over time into macroscopic chaos.",
         "Which choice best encapsulates the primary philosophical implication of Poincaré's mathematical finding?",
         "Physical systems governed by deterministic Newtonian laws can nonetheless be intrinsically unpredictable over extended time horizons.",
         ["Newton's universal law of gravitation is fundamentally invalid for multi-planetary systems.",
          "Algebraic solutions can always be discovered if measurement instruments possess infinite precision.",
          "The three-body problem can be resolved simply by approximating planetary masses as spherical coordinates."],
         "The passage explicitly concludes that 'determinism does not imply predictability': deterministic systems can amplify uncertainties exponentially into macroscopic chaos, making long-term prediction impossible."),

        # Q9: Inferences
        (DOMAINS["INFO"], "Inferences", "Hard",
         "High-pressure mineral physicists studying the Earth's mantle transition zone (410 to 660 kilometers depth) have discovered that wadsleyite and ringwoodite—high-pressure polymorphs of olivine—can incorporate up to 3% water by weight within their crystal lattices in the form of hydroxyl ions (OH-). Given the vast volumetric extent of the transition zone, if these minerals are even partially saturated, the mantle transition zone could hold as much water as all of Earth's surface oceans combined. Consequently, geophysicists hypothesize that deep-mantle dehydration melting _____.",
         "Which choice most logically completes the text?",
         "could play a profound, unappreciated role in modulating planetary-scale volatile cycling and mantle plume buoyancy over geological epochs.",
         ["proves that Earth's surface oceans were entirely drained from the mantle during the Pleistocene ice age.",
          "renders plate tectonic subduction physically impossible in oceanic lithospheric slabs.",
          "causes high-pressure olivine polymorphs to disintegrate immediately into atmospheric water vapor."],
         "If the mantle transition zone contains oceans' worth of water in crystal lattices, deep-mantle dehydration melting would significantly affect large-scale water/volatile cycling and mantle buoyancy over geological time."),

        # Q10: Command of Evidence (Textual)
        (DOMAINS["INFO"], "Command of Evidence", "Hard",
         "Archaeogeneticist Dr. Maria Lindqvist and her team analyzed ancient DNA extracted from Neolithic skeletal remains across the Scandinavian peninsula to test the 'cultural diffusion' versus 'demic diffusion' hypotheses for the spread of agriculture. Proponents of cultural diffusion argue that indigenous Mesolithic hunter-gatherers adopted farming technologies and cereal cultivation through trade and observational learning without substantial population turnover. Conversely, demic diffusion posits that expanding agriculturalist populations from Anatolia and Central Europe physically migrated into Scandinavia, largely supplanting the local foragers.",
         "Which finding, if true, would provide the strongest evidence in favor of the demic diffusion hypothesis?",
         "Skeletons associated with early Neolithic agricultural artifacts exhibited distinct West Eurasian genomic ancestry with virtually zero genetic continuity with earlier Mesolithic hunter-gatherer remains from the identical region.",
         ["Early farming implements uncovered in Scandinavian burial sites were crafted exclusively from locally quarried flint and birch wood.",
          "Isotopic analysis of dental enamel revealed that early Scandinavian farmers consumed marine-based protein diets identical to those of their hunter-gatherer ancestors.",
          "Ceramic pottery fragments from early agricultural settlements displayed decorative motifs identical to hunter-gatherer basketry."],
         "Demic diffusion requires physical population migration and turnover; finding distinct immigrant genomic ancestry and zero genetic continuity with earlier local foragers directly validates demic diffusion over cultural diffusion."),

        # Q11: Command of Evidence (Quantitative / Logic)
        (DOMAINS["INFO"], "Command of Evidence", "Hard",
         "In a double-blind trial evaluating immunotherapy in oncology, researchers measured tumor progression-free survival (PFS) in two groups of patients with stage IV melanoma. Cohort X received a monoclonal antibody targeting PD-1 receptors, while Cohort Y received a combined regimen targeting both PD-1 and CTLA-4 receptors. At 18 months, Cohort X exhibited a PFS rate of 34% with severe (Grade 3 or 4) autoimmune toxicity in 12% of patients. In contrast, Cohort Y exhibited a PFS rate of 58% but suffered severe autoimmune toxicity in 54% of patients.",
         "Which choice accurately synthesizes the clinical trade-off revealed by the study?",
         "Dual-checkpoint inhibition substantially enhanced tumor progression-free survival compared to single-agent therapy, but this therapeutic benefit was accompanied by a more than fourfold escalation in severe adverse toxicities.",
         ["Single-agent PD-1 therapy proved clinically superior in both survival rate and patient safety profile.",
          "Targeting CTLA-4 in conjunction with PD-1 completely eradicated severe autoimmune adverse events.",
          "Tumor progression was unaffected by the number of immune checkpoint pathways targeted simultaneously."],
         "Cohort Y improved PFS from 34% to 58% (substantial increase), but severe toxicities rose from 12% to 54% (more than 4.5 times greater)."),

        # Q12: Inferences / Logic Completion
        (DOMAINS["INFO"], "Inferences", "Hard",
         "In cognitive neuroscience, the 'Bayesian brain hypothesis' models perception as a process of probabilistic predictive coding: the brain continuously generates top-down generative models of sensory causes, comparing these predictions against incoming bottom-up sensory signals to compute 'prediction errors.' When a sensory prediction error occurs, the nervous system can either update its internal prior beliefs to accommodate the unexpected data or execute motor actions to align sensory inputs with expectations. Under this paradigm, persistent visual illusions occur because _____.",
         "Which choice most logically completes the text?",
         "the brain's robust prior beliefs about environmental statistics outweigh ambiguous or incomplete sensory inputs during probability integration.",
         ["sensory organs cease transmitting electrical signals to the primary visual cortex entirely.",
          "bottom-up sensory stimuli consistently override all pre-existing neural models and cognitive expectations.",
          "the brain possesses no internal generative models for resolving optical stimuli."],
         "In Bayesian predictive coding, illusions persist when the internal 'prior' (robust statistical expectation about light, shadows, perspective) is so strong that it overrides ambiguous sensory inputs."),

        # Q13: Standard English Conventions (Punctuation with Lists containing internal commas)
        (DOMAINS["CONV"], "Boundaries", "Hard",
         "The symposium featured presentations from prominent astrophysicists: Dr. Aris Thorne, who analyzed gravitational microlensing; Dr. Elena Rostova, who modeled cosmic microwave background _____ and Dr. Julian Vance, who presented high-resolution simulations of galactic accretion disks.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "anisotropies;",
         ["anisotropies,", "anisotropies", "anisotropies: and"],
         "When items in a series contain internal commas (e.g. 'Dr. Aris Thorne, who analyzed...'), the items must be separated by semicolons. Thus, 'anisotropies;' is required before 'and Dr. Julian Vance...'."),

        # Q14: Standard English Conventions (Inverted Syntax / Subject-Verb Agreement)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "Buried beneath three hundred meters of Antarctic glacial ice _____ a network of hyper-saline subglacial lakes that have remained isolated from atmospheric contact for over two million years.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "lies",
         ["lie", "are lying", "were lying"],
         "In this inverted sentence, the true grammatical subject is 'a network' (singular), which governs the verb. Therefore, the singular verb 'lies' is required."),

        # Q15: Standard English Conventions (Restrictive vs Non-restrictive Appositives)
        (DOMAINS["CONV"], "Boundaries", "Hard",
         "The pioneering botanist and conservationist _____ published her definitive field guide to the endangered flora of the Sonoran Desert in 1968, sparking nationwide legislative efforts to establish protected desert biomes.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "Gwendolyn Croft",
         ["Gwendolyn Croft,", ", Gwendolyn Croft,", ", Gwendolyn Croft"],
         "When a title or occupational descriptor precedes a name without an article ('The pioneering botanist and conservationist Gwendolyn Croft'), the name is restrictive and should not be set off by commas."),

        # Q16: Standard English Conventions (Parallelism with Correlative Conjunctions)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "The architectural committee insisted that the new performing arts pavilion must not only withstand the hurricane-force winds characteristic of the coastal estuary _____ the surrounding salt-marsh ecosystem by utilizing permeable recycled timber pilings.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "but also protect",
         ["and protecting", "but it protects", "along with protection of"],
         "The correlative conjunction 'not only [verb phrase]' must be paired with 'but also [verb phrase]': 'not only withstand... but also protect...'."),

        # Q17: Standard English Conventions (Dangling Modifiers)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "Employing scanning tunneling microscopy to manipulate individual xenon atoms on a chilled nickel substrate, _____ a micro-scale corporate logo that measured just fourteen nanometers across.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "IBM physicists fabricated",
         ["the fabrication was completed of", "a breakthrough was achieved by researchers with", "the manipulation resulted in"],
         "The introductory participial phrase 'Employing scanning tunneling microscopy...' must logically modify the grammatical subject immediately following the comma: 'IBM physicists'."),

        # Q18: Standard English Conventions (Subjunctive Mood / Modals)
        (DOMAINS["CONV"], "Form, Structure, and Sense", "Hard",
         "Because the newly discovered geothermal anomaly poses an immediate risk of catastrophic hydrothermal explosion, the head geologist recommended that the research station _____ immediately to a secure base camp outside the caldera.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "be evacuated",
         ["is evacuated", "was evacuated", "must to be evacuated"],
         "Verbs of demanding, suggesting, or recommending ('recommended that...') require the subjunctive mood base form: 'be evacuated'."),

        # Q19: Transitions
        (DOMAINS["EXPR"], "Transitions", "Hard",
         "Microeconomic models of perfect competition assume that all participating firms possess costless and instantaneous access to all relevant market information. In actual financial markets, _____, asymmetries in computational latency and proprietary data access grant high-frequency trading firms significant competitive advantages over retail investors.",
         "Which choice completes the text with the most logical transition?",
         "however,",
         ["likewise,", "moreover,", "in other words,"],
         "The theoretical assumption (costless, perfect access) is directly contrasted with real-world reality (informational asymmetries). 'However' is the precise contrastive transition."),

        # Q20: Transitions
        (DOMAINS["EXPR"], "Transitions", "Hard",
         "During the Great Oxygenation Event approximately 2.4 billion years ago, photosynthetic cyanobacteria produced molecular oxygen at unprecedented rates. _____, this biogenic oxygen reacted with dissolved ferrous iron in the oceans, precipitating massive banded iron formations that constitute humanity's primary iron ore deposits today.",
         "Which choice completes the text with the most logical transition?",
         "Initially,",
         ["On the contrary,", "Notwithstanding,", "Alternatively,"],
         "The sentence traces chronological biogeochemical progression: first cyanobacteria produced oxygen; 'Initially', that oxygen did not escape to the air but reacted with ferrous iron in the oceans."),

        # Q21: Transitions
        (DOMAINS["EXPR"], "Transitions", "Hard",
         "Quantum key distribution guarantees mathematically unconditional cryptographic security based on the laws of quantum mechanics rather than computational hardness assumptions. _____, if an eavesdropper attempts to intercept the transmitted photon stream, the physical act of measurement inevitably collapses the quantum state, alerting the legitimate communicating parties to the intrusion.",
         "Which choice completes the text with the most logical transition?",
         "Specifically,",
         ["Nonetheless,", "Conversely,", "Accordingly,"],
         "The second sentence elaborates on exactly how quantum key distribution works and achieves its security. 'Specifically' introduces the concrete physical mechanism."),

        # Q22: Rhetorical Synthesis
        (DOMAINS["EXPR"], "Rhetorical Synthesis", "Hard",
         "While researching a topic, a student has taken the following notes:\n- The 'Great Famine' of 1315–1317 in northern Europe was triggered by the onset of the Little Ice Age.\n- Torrential rains in spring 1315 caused widespread harvest failures and catastrophic flooding across Britain, northern France, and Germany.\n- Contemporary monastic chroniclers recorded that food shortages were so severe that millions died of starvation and disease.\n- Historical climatologists analyze oxygen isotope ratios in speleothems (cave mineral deposits) to reconstruct medieval precipitation patterns.\n- Speleothem records from Han-sur-Lesse cave in Belgium confirm that the years 1315 and 1316 experienced the most severe sustained deluge in northern Europe over the past thousand years.",
         "The student wants to demonstrate how contemporary scientific data corroborate medieval historical accounts of the Great Famine. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
         "Medieval monastic chronicles describing catastrophic rains and starvation during the 1315–1317 famine have been corroborated by oxygen isotope data from Belgian speleothems, which verify that 1315–1316 saw the most severe sustained deluge of the millennium.",
         ["Triggered by the Little Ice Age, the Great Famine of 1315–1317 caused widespread crop failure and starvation across northern Europe.",
          "Monastic chroniclers in Britain, France, and Germany wrote vivid accounts of severe food shortages during the fourteenth century.",
          "Historical climatologists can measure medieval European rainfall by analyzing oxygen isotope ratios in cave speleothems."],
         "Choice A explicitly links medieval monastic accounts with modern speleothem isotopic evidence, satisfying the prompt's objective of demonstrating scientific corroboration of historical chronicles."),

        # Q23: Rhetorical Synthesis
        (DOMAINS["EXPR"], "Rhetorical Synthesis", "Hard",
         "While researching a topic, a student has taken the following notes:\n- Polygenic risk scores (PRS) quantify an individual's genetic susceptibility to complex diseases by summing the weighted contributions of thousands of single-nucleotide polymorphisms (SNPs).\n- The vast majority of genome-wide association studies (GWAS) used to train PRS models have been conducted on cohorts of European genetic ancestry.\n- When a PRS trained on European cohorts is applied to individuals of African, East Asian, or Indigenous ancestry, its predictive accuracy drops by 50% to 80%.\n- This predictive disparity arises from differences in linkage disequilibrium patterns and allele frequencies across globally divergent populations.\n- Geneticists argue that expanding GWAS diversity is an urgent public health imperative to prevent clinical genetic medicine from exacerbating global healthcare inequalities.",
         "The student wants to emphasize the clinical limitation of current polygenic risk scores to an audience of medical students. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
         "Because current polygenic risk scores are disproportionately trained on European cohorts, their predictive accuracy drops by up to 80% when applied to non-European ancestry groups, presenting a critical barrier to equitable clinical implementation.",
         ["Polygenic risk scores estimate disease vulnerability by calculating the weighted impact of single-nucleotide polymorphisms across the human genome.",
          "Differences in linkage disequilibrium patterns and allele frequencies exist across populations of African, East Asian, and European descent.",
          "Genome-wide association studies must be expanded to include diverse global cohorts if researchers wish to understand the genetic architecture of disease."],
         "Choice A directly highlights the clinical limitation (up to 80% loss of predictive accuracy across diverse ancestries due to European cohort bias) and frames it as a medical barrier."),

        # Q24: Craft / Vocabulary / Tone
        (DOMAINS["CRAFT"], "Words in Context", "Hard",
         "The archival historian warned that applying twenty-first-century moral and political taxonomies to seventeenth-century ecclesiastical disputes creates an inherently _____ historical narrative that obscures the authentic motivations of historical actors.",
         "Which choice completes the text with the most logical and precise word or phrase?",
         "anachronistic",
         ["efficacious", "parsimonious", "pedantic"],
         "Imposing modern frameworks onto the 17th century is chronologically out of place. 'Anachronistic' means belonging or appropriate to an earlier period, or chronologically misplaced."),

        # Q25: Craft / Text Structure / Rhetorical Purpose
        (DOMAINS["CRAFT"], "Text Structure and Purpose", "Hard",
         "Philosopher Thomas Kuhn argued that science does not progress via the steady, cumulative accretion of objective facts, but rather through episodic paradigm shifts. During periods of 'normal science,' researchers operate within an unquestioned conceptual framework (paradigm), treating experimental anomalies not as refutations of the paradigm, but as puzzle-solving failures by the individual scientist. Only when anomalous data accumulate to an intolerable degree does the discipline enter a state of crisis, culminating in a scientific revolution that installs an entirely incommensurable paradigm.",
         "According to the passage, how do scientists during periods of 'normal science' typically interpret experimental findings that contradict dominant theoretical expectations?",
         "They attribute discrepancies to experimental error or methodological deficiencies on the part of the researcher rather than questioning the validity of the paradigm.",
         ["They immediately reject the reigning theoretical paradigm and formulate revolutionary explanatory frameworks.",
          "They publish revisionist treatises in an effort to initiate disciplinary crises and overthrow orthodox beliefs.",
          "They treat anomalies as definitive empirical mathematical proofs that universal physical constants are fluctuating."],
         "The text explicitly states: 'treating experimental anomalies not as refutations of the paradigm, but as puzzle-solving failures by the individual scientist.'"),

        # Q26: Standard English Conventions (Punctuation / Appositive Clauses)
        (DOMAINS["CONV"], "Boundaries", "Hard",
         "The mission team confirmed that the sample collection mechanism on the robotic _____ an intricate vacuum-sealed carousel designed to store pulverized Martian regolith—had successfully engaged without any loss of internal atmospheric pressure.",
         "Which choice completes the text so that it conforms to the conventions of Standard English?",
         "rover—",
         ["rover,", "rover;", "rover:"],
         "The parenthetical descriptive clause is closed with an em-dash ('—had successfully engaged'), so it must be opened with an em-dash ('rover—') for structural symmetry."),

        # Q27: Inferences / Advanced Reading
        (DOMAINS["INFO"], "Inferences", "Hard",
         "In evolutionary developmental biology ('evo-devo'), the concept of 'deep homology' describes how morphologically disparate structures in distantly related taxa—such as the compound eye of an arthropod and the camera-type eye of a vertebrate—are regulated by homologous genetic circuitry (such as the Pax6 master control gene). Because the common ancestor of arthropods and vertebrates possessed only primitive, non-image-forming photoreceptive pigment cups, evolutionary biologists infer that while the structural architecture of the complex eye evolved independently through convergent evolution, _____.",
         "Which choice most logically completes the text?",
         "the underlying genetic developmental program for photoreception was inherited from a shared bilaterian ancestor.",
         ["arthropods and vertebrates must have shared a common ancestor that possessed fully functional camera-type eyes.",
          "the Pax6 gene operates independently of all other transcriptional regulators in invertebrate embryogenesis.",
          "convergent morphological evolution cannot occur in organisms possessing homologous genetic pathways."],
         "The passage contrasts independent convergent structural evolution of eyes with homologous genetic circuitry (deep homology). Thus, while the complex eyes evolved independently, the underlying genetic program for photoreception was inherited from their common bilaterian ancestor.")
    ]
    
    questions = []
    for i, spec in enumerate(specs):
        qid = f"t4-rw2-q{i+1}"
        domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        target_letter = RW_TARGETS[i]
        questions.append(make_hard_mcq(qid, domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))
    return questions
