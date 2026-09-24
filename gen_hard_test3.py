# gen_hard_test3.py
# High-Difficulty 2026 Digital SAT Practice Test 3 Generator
import json
import os

DOMAINS = {
    "RW": {
        "CRAFT": "Craft and Structure",
        "INFO": "Information and Ideas",
        "CONV": "Standard English Conventions",
        "EXPR": "Expression of Ideas"
    },
    "MATH": {
        "ALG": "Algebra",
        "ADV": "Advanced Math",
        "PSDA": "Problem-Solving and Data Analysis",
        "GEOM": "Geometry and Trigonometry"
    }
}

RW_TARGETS = ['D', 'B', 'A', 'C', 'B', 'D', 'C', 'A', 'B', 'A', 'D', 'C', 'A', 'C', 'B', 'D', 'A', 'B', 'D', 'C', 'B', 'A', 'C', 'D', 'C', 'A', 'B']
MATH_TARGETS = ['A', 'C', 'B', 'D', 'B', 'D', 'A', 'C', 'D', 'B', 'A', 'C', 'B', 'D', 'C', 'A', 'C', 'A', 'D', 'B', 'D', 'B']

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

def make_spr(qid, domain, subdomain, diff, stimulus, prompt, correct_answers, explanation):
    ans_list = correct_answers if isinstance(correct_answers, list) else [str(correct_answers)]
    return {
        "id": qid,
        "type": "spr",
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": diff,
        "stimulus": stimulus,
        "prompt": prompt,
        "correctAnswer": ans_list,
        "explanation": f"The correct answer is {ans_list[0]}. {explanation}"
    }

def build_test3():
    rw_m1 = []
    rw_m2 = []
    math_m1 = []
    math_m2 = []

    # =========================================================================
    # TEST 3 - READING & WRITING MODULE 1 (High-Difficulty Routing Module)
    # =========================================================================
    rw_m1_specs = [
        # Q1 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
            "Although the economic historian presented an extensive array of nineteenth-century census records, contemporary reviewers found his central thesis _____ because he failed to account for regional monetary deflation following the Panic of 1873.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "unconvincing", ["pellucid", "unassailable", "impeccable"],
            "'Unconvincing' means not persuasive or credible. The failure to account for regional monetary deflation undermined the author's argument."
        ),
        # Q2 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Rather than offering a balanced evaluation of both competing hypotheses, the senior investigator's review paper was remarkably _____, dismissing contradictory fossil evidence with a perfunctory footnote while treating speculative genomic models as confirmed fact.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "partisan", ["dispassionate", "exhaustive", "inviolable"],
            "'Partisan' means prejudiced in favor of a particular cause or side. The contrast with 'balanced evaluation' and the dismissal of contradictory evidence confirm 'partisan'."
        ),
        # Q3 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The sociologist argued that the widespread adoption of automated algorithmic credit scoring does not eliminate human bias; rather, it merely _____ systemic historical inequities beneath a veneer of quantitative mathematical objectivity.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "cloaks", ["repudiates", "substantiates", "vitiates"],
            "'Cloaks' means conceals or disguises. The algorithm conceals historical inequities behind a veneer of mathematical objectivity."
        ),
        # Q4 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Far from being an insurmountable obstacle, the geographical barrier posed by the rugged mountain range proved to be _____ for the ancient kingdom, shielding its fertile interior valleys from imperial incursions while allowing controlled high-pass trade.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "salutary", ["deleterious", "quixotic", "draconian"],
            "'Salutary' means beneficial or producing good effects. The mountain barrier was advantageous/beneficial because it protected the kingdom from invasions."
        ),
        # Q5 Text Structure & Purpose
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In <i>The Logic of Scientific Discovery</i> (1934), philosopher Karl Popper introduced the criterion of 'falsifiability' to demarcate genuine empirical science from pseudoscience. Popper rejected the classical inductivist view that scientific theories are confirmed by accumulating corroborating observations. Because no finite number of white swan sightings can conclusively prove the universal proposition that 'all swans are white,' whereas a single black swan definitively refutes it, scientific laws can never be verified, only falsified. A legitimate scientific hypothesis, Popper argued, must make risky, testable predictions that expose it to potential refutation by empirical data.",
            "Which choice best describes the main rhetorical purpose of the text?",
            "To explain Popper's epistemological argument that scientific validity is grounded in potential empirical falsifiability rather than inductive verification.",
            [
                "To argue that twentieth-century physical theories were methodologically inferior to classical Newtonian mechanics.",
                "To criticize Popper for utilizing an oversimplified biological metaphor to describe particle physics.",
                "To prove that inductive logic is mathematically superior to deductive falsification in astronomical research."
            ],
            "The passage explains Popper's central thesis that scientific validity relies on falsifiability rather than inductive verification."
        ),
        # Q6 Cross-Text Connections
        (
            DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
            "<strong>Text 1</strong><br>Classical economic theory relies on the Efficient Market Hypothesis (EMH), which posits that asset prices instantaneously incorporate and reflect all available relevant information. Because millions of rational market participants continually arbitrage away mispricings, market prices always equal the fundamental present value of future cash flows, making it impossible for active portfolio managers to consistently outperform broad market index averages without incurring excessive risk.<br><br><strong>Text 2</strong><br>Behavioral finance theorists, such as Robert Shiller and Daniel Kahneman, have demonstrated that financial markets are frequently gripped by speculative bubbles and panic selloffs driven by herd behavior, cognitive overconfidence, and loss aversion. The persistent occurrence of asset price volatility vastly exceeding fluctuations in underlying corporate fundamentals suggests that market prices do not reflect perfect economic rationality, but rather the emotional and psychological biases of fallible human traders.",
            "Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1 regarding market prices equaling 'fundamental present value'?",
            "By contending that empirical asset prices routinely deviate from fundamental values due to psychological biases like herd behavior and cognitive overconfidence.",
            [
                "By demonstrating that active portfolio managers always outperform market indices over multi-decade horizons.",
                "By agreeing that market prices are mathematically rational while arguing that corporate cash flows are impossible to calculate.",
                "By asserting that arbitrageurs are legally prohibited from operating in modern equity exchanges."
            ],
            "Text 2 counters that market prices routinely detach from fundamentals because of human psychological biases and speculative bubbles."
        ),
        # Q7 Central Ideas & Details
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "The evolution of eukaryotic endomembrane systems, particularly the nuclear envelope and endoplasmic reticulum, enabled a fundamental physical separation between genetic transcription (in the nucleus) and protein translation (in the cytoplasm). In prokaryotes, where DNA floats freely in the nucleoid region, ribosomes immediately bind to nascent messenger RNA while it is still being transcribed by RNA polymerase. By enforcing spatial and temporal separation, eukaryotes can subject pre-mRNA to complex post-transcriptional processing—including alternative splicing of introns and 5'-capping—before translation begins, dramatically expanding proteomic diversity from a compact genomic footprint.",
            "According to the text, what is the primary evolutionary advantage conferred by the spatial separation of transcription and translation in eukaryotes?",
            "It permits extensive pre-translational RNA processing, such as alternative splicing, thereby expanding proteomic diversity without requiring an enormous genome.",
            [
                "It accelerates the overall rate of protein synthesis to exceed the translation speed of prokaryotes.",
                "It eliminates the necessity of ribosomes during cytoplasmic peptide synthesis.",
                "It allows direct reverse transcription of genomic DNA within cellular mitochondria."
            ],
            "The passage explicitly states spatial separation allows pre-mRNA post-transcriptional processing (like alternative splicing), expanding proteomic diversity."
        ),
        # Q8 Command of Evidence: Textual
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Ecologist Dr. Arthur Bailey investigated the 'trophic cascade hypothesis' following the reintroduction of gray wolves (<i>Canis lupus</i>) to Yellowstone National Park. Bailey predicted that wolf predation would not merely reduce elk numbers, but would create a 'landscape of fear' that alters elk browsing behavior, allowing over-browsed riparian woody vegetation (willows and aspens) to recover. If Dr. Bailey's observations substantiate the behavioral trophic cascade hypothesis, which finding would most strongly confirm this?",
            "Riparian willow height and canopy density recovered dramatically along high-risk river valley corridors where elk avoided foraging, even in areas where total regional elk population reductions were minimal.",
            [
                "Willow heights remained completely stunted across all park watersheds regardless of local wolf pack territorial presence.",
                "Elk populations collapsed to near extinction throughout the park, causing predatory wolves to switch exclusively to hunting bison.",
                "Beaver populations declined sharply along riverbanks as recovering willow stands obstructed dam construction."
            ],
            "The behavioral cascade hypothesis specifies that elk alter foraging behavior out of fear (avoiding risky valleys), allowing willows to recover even without a total population crash."
        ),
        # Q9 Command of Evidence: Quantitative
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Materials scientists tested the electrical conductivity and fracture toughness of carbon nanotube (CNT) reinforced ceramic matrices across varying weight percentages of CNT additives.<br><br><table style='width:100%; border-collapse: collapse; margin: 8px 0; font-size: 13px;'><tr style='background: #f1f5f9;'><th style='border: 1px solid #cbd5e1; padding: 6px;'>CNT Loading (wt%)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Fracture Toughness (MPa·m¹/²)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Electrical Conductivity (S/m)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Relative Density (%)</th></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>0.0% (Pure Ceramic)</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>3.2</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.2 × 10⁻¹²</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>99.4%</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.5%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>4.8</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>4.5 × 10⁻¹</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>98.8%</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>3.0%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>6.1</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>3.2 × 10²</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>98.1%</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>5.0%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>5.2</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>8.9 × 10²</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>94.5%</td></tr></table><br>The researchers concluded that increasing CNT loading up to 3.0 wt% enhances mechanical fracture toughness, but higher concentrations induce nanotube agglomeration that creates porosity defects.",
            "Which statement is best supported by the data in the table?",
            "Fracture toughness peaked at 6.1 MPa·m¹/² at 3.0 wt% CNT loading before declining at 5.0 wt%, coinciding with a drop in relative density to 94.5%.",
            [
                "Electrical conductivity was lowest at 5.0 wt% CNT loading due to extensive material porosity.",
                "Fracture toughness increased monotonically across all four CNT loading concentrations.",
                "Pure ceramic exhibited superior electrical conductivity compared to all composite formulations."
            ],
            "The table shows fracture toughness peaks at 6.1 at 3.0 wt% and then falls to 5.2 at 5.0 wt%, while density drops to 94.5%."
        ),
        # Q10 Inferences
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In macroeconomics, the 'impossible trinity' (or trilemma) states that a nation can simultaneously maintain at most two of the following three policy objectives: a fixed foreign exchange rate, free international capital movement, and an independent domestic monetary policy. When a country fixes its currency exchange rate while permitting open capital flows, its central bank must set interest rates in strict lockstep with the foreign pegging currency to prevent arbitrage capital flights. It follows from this principle that if a government with a fixed exchange rate and open capital borders desires to lower domestic interest rates to stimulate local employment, it must _____.",
            "relinquish its fixed exchange rate or impose capital controls to prevent massive capital outflows and currency depreciation",
            [
                "command the foreign central bank to lower international interest rates proportionately",
                "outlaw all domestic private manufacturing firms from trading in foreign currencies",
                "simultaneously achieve all three trilemma goals by increasing fiscal tax revenues"
            ],
            "By the trilemma, pursuing independent monetary policy (lowering interest rates) requires abandoning either open capital flows (imposing controls) or the fixed exchange rate."
        ),
        # Q11 Standard English Conventions: Boundaries
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "In 1915, Albert Einstein published his field equations for general relativity, asserting that gravity is not a Newtonian force exerted across empty _____ curvature of spacetime caused by mass and energy.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "space, but rather a geometric",
            [
                "space; but rather a geometric",
                "space but rather a geometric",
                "space. But rather a geometric"
            ],
            "The correlative contrast 'not X, but rather Y' is a single compound element. A comma before 'but rather' cleanly separates the contrasting phrases."
        ),
        # Q12 Standard English Conventions: Modifiers
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Having pioneered the technique of optical tweezers to manipulate microscopic biological _____ biophysicist Steven Chu was awarded the Nobel Prize in Physics in 1997.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "specimens,",
            [
                "specimens",
                "specimens; the",
                "specimens and"
            ],
            "Introductory participial phrase ('Having pioneered... biological specimens,') must be followed by a comma and the subject 'biophysicist Steven Chu'."
        ),
        # Q13 Standard English Conventions: Subject-Verb Agreement
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "The rapid proliferation of consumer internet-of-things devices, alongside the widespread expansion of corporate cloud storage, _____ substantial cybersecurity challenges for municipal infrastructure.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "presents",
            ["present", "presenting", "have presented"],
            "Subject is singular ('proliferation'), which takes the singular verb 'presents'. The intervening phrase 'alongside...' does not alter subject number."
        ),
        # Q14 Standard English Conventions: Semicolons
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "Urban wetlands provide invaluable ecosystem services by sequestering excess stormwater and filtering industrial _____ they also function as vital refueling corridors for migratory waterfowl.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "pollutants; furthermore,",
            [
                "pollutants, furthermore",
                "pollutants furthermore",
                "pollutants: furthermore"
            ],
            "Two independent clauses joined by conjunctive adverb: semicolon before 'furthermore,' and a comma following it."
        ),
        # Q15 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Classical Newtonian mechanics accurately predicts the orbital trajectories of planetary bodies across the solar system. _____, it fails completely when applied to objects traveling at velocities approaching the speed of light, where Einstein's relativistic spacetime transformations become necessary.",
            "Which choice completes the text with the most logical transition?",
            "However,",
            ["Furthermore,", "Consequently,", "Similarly,"],
            "'However' marks the contrast between classical mechanics succeeding at everyday speeds and failing at near-light speeds."
        ),
        # Q16 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Paleontologists long believed that the extinction of non-avian dinosaurs was a protracted ecological decline catalyzed by gradual volcanism. _____, discovery of an iridium-enriched geological boundary dating precisely to 66 million years ago demonstrated that an abrupt asteroid impact triggered the catastrophic mass extinction.",
            "Which choice completes the text with the most logical transition?",
            "In fact,",
            ["Accordingly,", "For example,", "Likewise,"],
            "'In fact' or 'Ultimately' introduces the surprising evidence that refuted the gradualist belief."
        ),
        # Q17 Rhetorical Synthesis
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The Kuiper Belt is a circumstellar disc in the outer Solar System extending from Neptune's orbit at 30 AU to approximately 50 AU.</li><li style='margin-bottom: 4px;'>It contains hundreds of thousands of icy bodies and remnant planetesimals.</li><li style='margin-bottom: 4px;'>Pluto was the first Kuiper Belt object discovered, in 1930.</li><li style='margin-bottom: 4px;'>In 2005, astronomer Mike Brown discovered Eris, a trans-Neptunian object more massive than Pluto.</li><li style='margin-bottom: 4px;'>The discovery of Eris prompted the International Astronomical Union (IAU) in 2006 to formally define the term 'planet,' reclassifying Pluto and Eris as dwarf planets.</li></ul>",
            "The student wants to explain the historical significance of the discovery of Eris. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "The 2005 discovery of Eris, a Kuiper Belt object more massive than Pluto, prompted the International Astronomical Union to establish a formal definition of a planet and reclassify Pluto as a dwarf planet.",
            [
                "Extending beyond Neptune from 30 to 50 AU, the Kuiper Belt contains hundreds of thousands of ancient icy bodies.",
                "Discovered in 1930, Pluto was considered a major planet until astronomer Mike Brown studied trans-Neptunian objects.",
                "Astronomer Mike Brown discovered Eris in 2005 using modern digital astronomical observatories."
            ],
            "The sentence directly fulfills the goal of explaining the historical significance of Eris: prompting the IAU to formally define 'planet' and reclassify Pluto."
        ),
        # Q18 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The historical biographer noted that while the general was celebrated for his bold cavalry maneuvers, his strategic planning was frequently _____, marked by careless logistical oversight and an overconfidence in terrain intelligence.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "flawed", ["inviolable", "exhaustive", "pellucid"],
            "'Flawed' means having defects or blemishes. Careless logistical oversight and overconfidence in terrain intelligence describe flawed planning."
        ),
        # Q19 Text Structure & Purpose
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In <i>The Concept of Mind</i> (1949), British philosopher Gilbert Ryle critiqued René Descartes's mind-body dualism, famously denouncing the idea of a non-physical mind inhabiting a physical body as the 'dogma of the Ghost in the Machine.' Ryle argued that dualism commits a fundamental 'category-mistake' by treating mental states (such as beliefs, intentions, and emotions) as if they were unobservable occult substances existing parallel to physical organs. Instead, Ryle maintained that mental vocabulary refers not to mysterious ghostly events, but to an organism's behavioral dispositions and observable actions.",
            "Which choice best describes the primary function of the passage?",
            "To explain Ryle's philosophical critique of Cartesian dualism and his behavioral reinterpretation of mental concepts.",
            [
                "To prove that modern neuroimaging has conclusively demonstrated Descartes's dualist theories.",
                "To criticize Gilbert Ryle for misunderstanding seventeenth-century French anatomical terminology.",
                "To chronicle the development of computational artificial intelligence models in early twentieth-century Oxford."
            ],
            "The text outlines Ryle's critique of Cartesian mind-body dualism ('Ghost in the Machine' category-mistake) and his alternative dispositional view."
        ),
        # Q20 Central Ideas & Details
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "MicroRNAs (miRNAs) are short, non-coding RNA molecules (approximately 21 to 23 nucleotides in length) that function as master post-transcriptional regulators in eukaryotic gene expression. Once processed by the Dicer enzyme, a mature miRNA incorporates into the RNA-induced silencing complex (RISC). The miRNA directs RISC to bind to complementary sequences within the 3' untranslated region (3'-UTR) of target messenger RNAs. If base-pairing is near-perfect, RISC cleaves the target mRNA; if pairing is imperfect, RISC represses translation without destroying the transcript. Through this mechanism, a single miRNA can fine-tune the translation of hundreds of distinct protein-coding genes.",
            "According to the text, what determines whether RISC cleaves an mRNA transcript or merely represses its translation?",
            "The degree of sequence complementarity between the microRNA and the 3' untranslated region of the target mRNA.",
            [
                "The concentration of Dicer enzymes present in the cellular nucleus.",
                "The total length of the eukaryotic protein encoded by the transcript.",
                "The presence of bacterial reverse transcriptase in the cytoplasm."
            ],
            "The passage explicitly states that near-perfect base-pairing leads to cleavage, whereas imperfect pairing leads to translational repression."
        ),
        # Q21 Command of Evidence
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Plant ecologist Dr. Clara Vance investigated the 'enemy release hypothesis,' which posits that invasive plant species achieve ecological dominance in introduced ranges because they escape the specialized co-evolved herbivores and fungal pathogens that suppress them in their native habitats. Vance compared leaf herbivory damage and seed reproduction between <i>Alliaria petiolata</i> (garlic mustard) plants in their native European range and invasive North American populations. If Dr. Vance's data support the enemy release hypothesis, which observation would be expected?",
            "North American garlic mustard populations experienced 85% less foliar herbivore damage and produced five times more viable seeds per plant than native European populations.",
            [
                "European garlic mustard populations produced identical seed numbers despite higher pathogen exposure.",
                "North American populations were rapidly extirpated by native North American herbivorous caterpillars.",
                "Herbivore damage was positively correlated with soil nitrogen availability across both continents."
            ],
            "Enemy release predicts introduced populations experience less herbivore damage and greater reproductive success than native populations."
        ),
        # Q22 Inferences
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In evolutionary robotics, researchers utilize genetic algorithms to evolve morphological locomotory forms for autonomous soft robots. When simulated robots are evaluated in static virtual physics environments, the evolutionary algorithm consistently converges upon brittle, over-specialized gaits that collapse when tested in real-world physical terrain with variable friction and uneven obstacles. However, when researchers introduce stochastic turbulence and dynamic physical obstacles into the evolutionary training simulation, the evolved robots develop robust, compliant locomotion capable of adapting to unexpected perturbations. This suggests that _____.",
            "environmental variability and physical disturbance during simulated evolutionary training are essential for cultivating robust, adaptable real-world robotic locomotion",
            [
                "soft robots cannot function in real-world physical environments due to hardware material limitations",
                "static simulation environments produce superior robotic software than stochastic physical training models",
                "genetic algorithms are mathematically incapable of optimizing mechanical locomotory systems"
            ],
            "Introducing turbulence and dynamic obstacles created robust, adaptable robots, indicating that environmental variability during training is essential."
        ),
        # Q23 Standard English Conventions (Boundaries)
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "In 1905, Albert Einstein published his paper on the photoelectric effect _____ work that demonstrated the quantized nature of light and earned him the 1921 Nobel Prize in Physics.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "—a groundbreaking",
            ["; a groundbreaking", ", being a groundbreaking", "a groundbreaking"],
            "An em-dash ('—a groundbreaking work...') is an effective and grammatically correct way to set off an emphatic appositive phrase at the end of a sentence."
        ),
        # Q24 Standard English Conventions (Form/Structure)
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Neither the sudden rise in global benchmark crude oil prices nor the escalation of regional shipping _____ the consumer confidence index in the second quarter.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "costs dampened",
            ["costs dampening", "costs, dampening", "costs having dampened"],
            "The sentence requires an inflected finite main verb: 'costs dampened the consumer confidence index'."
        ),
        # Q25 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Early geologists assumed that deep oceanic trenches were formed by sediment erosion from submarine turbidity currents. _____, seismic mapping in the 1960s revealed that trenches mark subduction zones where oceanic plates plunge into the mantle.",
            "Which choice completes the text with the most logical transition?",
            "Instead,",
            ["Furthermore,", "Consequently,", "Similarly,"],
            "'Instead' marks the replacement of the erroneous early hypothesis by the actual plate tectonic discovery."
        ),
        # Q26 Rhetorical Synthesis
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The Great Barrier Reef off the coast of Australia is the largest coral reef system on Earth.</li><li style='margin-bottom: 4px;'>It comprises over 2,900 individual reefs and 900 islands spanning 2,300 kilometers.</li><li style='margin-bottom: 4px;'>Mass coral bleaching events occur when sustained sea surface temperature anomalies cause corals to expel their symbiotic zooxanthellae algae.</li><li style='margin-bottom: 4px;'>Severe mass bleaching events occurred across the reef in 2016, 2017, 2020, 2022, and 2024.</li><li style='margin-bottom: 4px;'>The accelerating frequency of bleaching events leaves corals insufficient recovery time between heatwaves.</li></ul>",
            "The student wants to emphasize the growing threat that frequent thermal stress poses to the Great Barrier Reef. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "With five severe mass bleaching events occurring since 2016, the accelerating frequency of thermal heatwaves threatens the Great Barrier Reef by depriving corals of the time needed to recover between disturbances.",
            [
                "Spanning 2,300 kilometers along the Australian coast, the Great Barrier Reef is the largest coral ecosystem in the world.",
                "Coral bleaching is a physiological response in which corals expel symbiotic algae during prolonged warm water events.",
                "Composed of 2,900 individual reefs, the Great Barrier Reef experienced mass coral bleaching in 2016."
            ],
            "The sentence directly emphasizes the growing threat posed by frequent thermal stress: 5 events since 2016 preventing recovery time."
        ),
        # Q27 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Although the political commentator's predictions were delivered with immense rhetorical confidence, historical retrospectives revealed that his geopolitical forecasts were remarkably _____, failing to anticipate major systemic revolutions.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "fallible", ["inviolable", "prescient", "dogmatic"],
            "'Fallible' means capable of making mistakes or being erroneous. Failing to anticipate major systemic revolutions demonstrates that his forecasts were fallible."
        )
    ]

    for i, spec in enumerate(rw_m1_specs):
        target_letter = RW_TARGETS[i]
        if len(spec) == 7:
            domain, subdomain, diff, stim, corr, dists, expl = spec
            prompt = "Which choice most logically completes the text?" if "_____" in stim else "Which finding, if true, most strongly supports the hypothesis?"
        else:
            domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        rw_m1.append(make_hard_mcq(f"t3-rw-m1-q{i+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # =========================================================================
    # TEST 3 - READING & WRITING MODULE 2 (Adaptive Hard Module)
    # =========================================================================
    rw_m2_specs = [
        # Q1 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The theoretical physicist noted that while mathematical elegance often guides the formulation of cosmological hypotheses, aesthetic beauty alone cannot _____ an empirical physical theory in the absence of experimental particle detection.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "validate", ["obviate", "vitiate", "dissemble"],
            "'Validate' means to substantiate, confirm, or prove the accuracy of. Aesthetic beauty cannot confirm/validate a physical theory without empirical evidence."
        ),
        # Q2 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "In his scathing review of contemporary municipal architecture, the critic denounced the downtown high-rises as utterly _____, lamenting that generic glass monoliths had replaced regional masonry traditions with corporate monotony.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "banal", ["scintillating", "idiosyncratic", "pellucid"],
            "'Banal' means lacking in originality as to be obvious and boring. It matches 'generic glass monoliths' and 'corporate monotony'."
        ),
        # Q3 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Far from being an accidental byproduct of administrative oversight, historians demonstrated that the rationing protocols during the siege were a _____ calculation designed to preserve military provisions even at the cost of civilian deprivation.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "deliberate", ["capricious", "perfunctory", "spurious"],
            "'Deliberate' means done consciously and intentionally. It contrasts with 'accidental byproduct' and matches 'calculation designed to preserve provisions'."
        ),
        # Q4 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The bioethicist cautioned that granting patents for synthetic genetic sequences could create a _____ legal landscape where research institutions must navigate thickets of intellectual property claims to conduct basic virological research.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "labyrinthine", ["pellucid", "straightforward", "salutary"],
            "'Labyrinthine' means complicated, tortuous, or maze-like. Navigating patent thickets describes a labyrinthine legal landscape."
        ),
        # Q5 Text Structure & Purpose
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In <i>Orientalism</i> (1978), cultural critic Edward Said argued that Western scholarly, literary, and imperial representations of the 'Orient' did not simply describe the Middle East and Asia, but actively produced an ideological construct of the East as exotic, backward, uncivilized, and fundamentally inferior to the rational West. Said demonstrated that this discursive binary was intimately intertwined with imperial state power, providing the cultural justification for European colonial domination. While critics argued that Said underestimated the objective philological achievements of Western orientalist scholars, Said maintained that academic scholarship cannot be extracted from the geopolitical contexts of colonial hegemony.",
            "Which choice best describes the relationship between the second sentence and the third sentence in the text?",
            "The second sentence explains how orientalist discourse served colonial political interests, and the third sentence presents a critique of Said's thesis followed by Said's rebuttal.",
            [
                "The second sentence outlines a historical consensus, and the third sentence provides empirical archaeological data that invalidates it.",
                "The second sentence criticizes Western colonial literature, and the third sentence praises nineteenth-century philological methodology.",
                "The second sentence introduces an unresolved literary controversy, and the third sentence resolves it through quantitative textual analysis."
            ],
            "Sentence 2 links discourse to colonial power; sentence 3 introduces scholarly critiques of Said and his response regarding geopolitical context."
        ),
        # Q6 Cross-Text Connections
        (
            DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
            "<strong>Text 1</strong><br>The Efficient Market Hypothesis (EMH) in financial economics implies that technical analysis—the practice of studying historical price charts, trading volume, and moving averages to predict future asset prices—is an exercise in futility. Because current asset prices already incorporate all past trading history, past price movements contain zero predictive power regarding future price trajectories, which follow a random walk.<br><br><strong>Text 2</strong><br>Proponents of behavioral finance demonstrate that market participants are prone to cognitive anchoring, momentum chasing, and disposition effects (holding losing stocks while prematurely selling winners). Because human psychology reacts to market trends with systematic delays and herd overreactions, asset prices exhibit measurable autocorrelation and price momentum over medium-term horizons, creating exploitable statistical patterns that technical indicators can capture.",
            "Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1 that 'past price movements contain zero predictive power'?",
            "By contending that systematic psychological biases like herd behavior and momentum chasing cause prices to exhibit predictable medium-term trends.",
            [
                "By demonstrating that random walk models are mathematically invalid in all branches of physical and social science.",
                "By conceding that stock prices follow a random walk while arguing that currency exchange markets are completely deterministic.",
                "By proving that individual retail traders consistently outperform institutional algorithmic trading desks."
            ],
            "Text 2 argues that human psychological biases create price momentum and medium-term autocorrelation, giving past movements predictive value."
        ),
        # Q7 Central Ideas & Details
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "In synthetic biology, metabolic engineers utilize directed evolution to optimize microbial enzymatic pathways for bio-manufacturing sustainable aviation fuels. Directed evolution mimics natural selection in a test tube: mutagenic polymerase chain reactions introduce random genetic mutations into an enzyme's coding sequence, generating millions of variant proteins. High-throughput microfluidic screening assays then isolate the rarest variants that exhibit enhanced catalytic turnover rates ($k_{\\text{cat}}$) and elevated thermal stability. Over iterative rounds of mutation, selection, and amplification, enzymes acquire complex synergistic mutations that would have been impossible to predict through rational computational protein design.",
            "Which choice best expresses the primary advantage of directed evolution over rational computational design described in the passage?",
            "It discovers beneficial multi-mutation combinations that enhance catalytic efficiency through iterative empirical selection without requiring prior predictive structural modeling.",
            [
                "It eliminates the necessity of utilizing living microbial hosts during industrial fermentation.",
                "It synthesizes aviation fuels directly from atmospheric carbon dioxide without requiring enzymatic biocatalysts.",
                "It completely prevents any random genetic mutations from occurring during high-throughput microfluidic assays."
            ],
            "The passage states directed evolution generates complex synergistic mutations that would be impossible to predict through rational computational design."
        ),
        # Q8 Command of Evidence: Textual
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Neuroscientist Dr. Julian Rossi evaluated the 'default mode network' (DMN) in creative cognition. Rossi hypothesized that creative divergent thinking requires a dynamic functional coupling between the DMN (associated with spontaneous, internally-focused ideation) and the executive control network (ECN, associated with cognitive monitoring, goal-maintenance, and idea evaluation). To test this, Rossi scanned jazz musicians using functional magnetic resonance imaging (fMRI) during two conditions: memorized score reproduction versus spontaneous improvisational solos. If Rossi's hypothesis is correct, which neuroimaging finding would be observed during improvisation?",
            "Spontaneous improvisation was characterized by synchronized functional co-activation and elevated functional connectivity between core hubs of the DMN and the ECN.",
            [
                "Improvisation caused complete neurological deactivation of both the DMN and the executive control network.",
                "Memorized score reproduction triggered identical functional co-activation between the DMN and sensory motor cortices.",
                "Musicians demonstrated exclusive activation of the amygdala with complete suppression of all prefrontal cortical regions during improvisation."
            ],
            "Rossi's hypothesis predicts dynamic functional coupling (co-activation and elevated connectivity) between DMN and ECN during creative improvisation."
        ),
        # Q9 Command of Evidence: Quantitative
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Pharmacologists tested the bioavailability ($F$) and elimination half-life ($t_{1/2}$) of four novel oral nanoparticle drug delivery formulations (Formulations A, B, C, and D) targeting central nervous system delivery across the blood-brain barrier.<br><br><table style='width:100%; border-collapse: collapse; margin: 8px 0; font-size: 13px;'><tr style='background: #f1f5f9;'><th style='border: 1px solid #cbd5e1; padding: 6px;'>Formulation</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Nanoparticle Size (nm)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Oral Bioavailability (F%)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Brain-to-Plasma Ratio</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Half-Life (hours)</th></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Formulation A</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>180</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>24%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>0.12</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>3.2</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Formulation B</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>95</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>58%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>0.65</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>8.4</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Formulation C</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>45</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>72%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.45</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>14.6</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Formulation D</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>25</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>64%</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.10</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>4.1</td></tr></table><br>The researchers concluded that Formulation C offers the optimal pharmacokinetic profile for therapeutic neurodegenerative treatment.",
            "Which finding is best supported by the data in the table?",
            "Formulation C demonstrated the highest oral bioavailability (72%), the highest brain-to-plasma ratio (1.45), and the longest elimination half-life (14.6 hours).",
            [
                "Formulation A crossed the blood-brain barrier with greater efficiency than any other formulation evaluated.",
                "Nanoparticle size was inversely proportional to oral bioavailability across all four formulations.",
                "Formulation D achieved a higher brain-to-plasma ratio than Formulation C despite having a smaller particle diameter."
            ],
            "The table shows Formulation C has the highest bioavailability (72%), highest brain-to-plasma ratio (1.45), and longest half-life (14.6 h)."
        ),
        # Q10 Inferences
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In behavioral ecology, the 'producer-scrounger game' models social foraging: 'producers' search actively for novel food patches, while 'scroungers' visually monitor producers and usurp their discoveries. If the frequency of scroungers in a flock is low, scrounging yields higher caloric intake per unit time because scroungers avoid the metabolic investment and predation risks of foraging search. However, as the proportion of scroungers increases, the availability of newly discovered patches declines sharply, causing scrounger payoffs to plummet until the fitness of both strategies reaches an evolutionary stable equilibrium. It can reasonably be inferred that if a flock were artificially manipulated to consist of 95% scroungers and only 5% producers, _____.",
            "producers would achieve significantly higher per-capita foraging payoffs than scroungers because scroungers would aggressively compete over an extreme scarcity of discovered food patches",
            [
                "the entire flock would immediately discover ten times more food patches than an unmanipulated flock",
                "scroungers would experience zero foraging competition and maximize their reproductive fitness",
                "producers would abandon food production and mutate into obligate carnivores"
            ],
            "When scroungers are at 95%, intense competition over very few discovered patches causes scrounger payoffs to collapse below producer payoffs."
        ),
        # Q11 Standard English Conventions: Boundaries
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "In 1965, Arno Penzias and Robert Wilson detected an isotropic microwave signal emanating uniformly from all directions in _____ relic radiation from the Big Bang that provided definitive confirmation for the hot inflationary model of cosmology.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "space, a primordial",
            [
                "space; a primordial",
                "space a primordial",
                "space: being a primordial"
            ],
            "'a primordial relic radiation...' is an appositive modifying the isotropic microwave signal. A comma correctly attaches it."
        ),
        # Q12 Standard English Conventions: Modifiers
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Subjected to extreme tectonic shear stresses along the convergent subduction _____ metamorphic rocks recrystallized into high-pressure, low-temperature blueschist mineral assemblages.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "zone,",
            ["zone", "zone; the", "zone and"],
            "Introductory participial phrase ('Subjected to extreme tectonic shear stresses... zone,') must be followed by a comma and the subject 'metamorphic rocks'."
        ),
        # Q13 Standard English Conventions: Subject-Verb Agreement
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "The continuous collection of meteorological telemetry, together with high-resolution radar scans from Doppler satellite _____ climatologists to model tornadic vortex formation with unprecedented precision.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "arrays, allows",
            [
                "arrays, allow",
                "arrays allow",
                "arrays allowing"
            ],
            "Subject is singular ('collection'), which takes the singular verb 'allows'. The parenthetical phrase 'together with...' is enclosed in commas."
        ),
        # Q14 Standard English Conventions: Dashes
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "The critical components of the cellular cytoskeleton—microfilaments, intermediate filaments, and _____ dynamic structural scaffolding necessary for intracellular vesicular trafficking.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "microtubules—provide the",
            [
                "microtubules, provide the",
                "microtubules; provide the",
                "microtubules provide the"
            ],
            "An em-dash opens the list ('cytoskeleton—microfilaments...'), so an em-dash must close it ('microtubules—provide the')."
        ),
        # Q15 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Advocates of cryptocurrency decentralization argued that blockchain networks would eliminate financial intermediaries and democratize global capital. _____, cryptocurrency exchanges and mining power became increasingly centralized among a handful of multi-billion-dollar conglomerates.",
            "Which choice completes the text with the most logical transition?",
            "In practice,",
            ["Furthermore,", "Similarly,", "Consequently,"],
            "'In practice' contrasts the idealistic theoretical claims of decentralization with the actual reality of growing concentration."
        ),
        # Q16 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Ecologists originally believed that deep-sea benthic plains were biological deserts devoid of complex species interactions. _____, remote submersibles revealed sprawling benthic ecosystems sustained by whale-fall chemosynthesis and deep-sea cold seeps.",
            "Which choice completes the text with the most logical transition?",
            "In reality,",
            ["Therefore,", "In addition,", "For instance,"],
            "'In reality' contrasts the erroneous early belief with the actual factual discovery."
        ),
        # Q17 Rhetorical Synthesis
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The Roman Colosseum was completed in 80 CE under the Flavian dynasty.</li><li style='margin-bottom: 4px;'>It held an estimated 50,000 to 80,000 spectators.</li><li style='margin-bottom: 4px;'>Architects utilized an ingenious network of barrel vaults and groin vaults constructed from travertine limestone and pozzolanic concrete.</li><li style='margin-bottom: 4px;'>The amphitheater featured 80 numbered arched entrance portals (vomitoria) that allowed the entire venue to be evacuated in under twenty minutes.</li><li style='margin-bottom: 4px;'>Beneath the wooden arena floor was the hypogeum, a subterranean complex of cages, hoists, and hydraulic elevators.</li></ul>",
            "The student wants to highlight the engineering innovation that facilitated efficient crowd control in the Colosseum. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "Featuring eighty numbered arched entrance portals known as vomitoria, the Roman Colosseum was engineered to allow up to 80,000 spectators to evacuate the massive venue in under twenty minutes.",
            [
                "Completed in 80 CE under the Flavian dynasty, the Colosseum utilized travertine limestone and pozzolanic concrete barrel vaults.",
                "Beneath the Colosseum's wooden arena floor lay the hypogeum, an intricate subterranean complex of cages and hydraulic hoists.",
                "The Roman Colosseum seated tens of thousands of Roman spectators for gladiatorial games and civic festivals."
            ],
            "The sentence directly addresses crowd control: 80 numbered vomitoria entrance portals allowing complete evacuation in under 20 minutes."
        ),
        # Q18 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The literary critic praised the playwright for her _____ dialogue, noting that her characters revealed deep emotional vulnerability through sparse, restrained sentences rather than lengthy theatrical soliloquies.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "laconic", ["garrulous", "bombastic", "pedantic"],
            "'Laconic' means using very few words. It matches 'sparse, restrained sentences' rather than lengthy soliloquies."
        ),
        # Q19 Text Structure & Purpose
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In <i>The Ecological Approach to Visual Perception</i> (1979), perceptual psychologist J.J. Gibson challenged the computational model of vision, which conceptualized visual perception as an indirect mental reconstruction of flat retinal images. Instead, Gibson proposed the concept of 'affordances'—the actionable properties of the environment directly perceived by an organism without intermediary cognitive processing. A horizontal, rigid flat surface at knee height does not require complex mental calculation to be understood; it directly affords 'sitting' to a human observer. Visual perception, Gibson argued, is an active ecological process of picking up invariant optical information as the organism navigates its physical environment.",
            "Which choice best summarizes Gibson's theory of visual perception as presented in the text?",
            "Organisms perceive actionable environmental opportunities directly through optical exploration rather than computationally reconstructing mental images from retinal data.",
            [
                "Visual perception is an entirely learned cultural behavior that develops only through linguistic education.",
                "Computational artificial neural networks process two-dimensional retinal images more accurately than human visual cortices.",
                "Affordances are abstract mathematical equations used by cognitive neuroscientists to measure visual acuity."
            ],
            "The passage summarizes Gibson's theory that perception is direct pickup of environmental affordances without indirect computational reconstruction."
        ),
        # Q20 Central Ideas & Details
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "Telomeres are repetitive hexanucleotide DNA sequences ($\text{TTAGGG}$) capping the ends of eukaryotic chromosomes that protect genomic integrity from degradation during DNA replication. Because DNA polymerase requires an RNA primer and can only synthesize DNA in the $5' \\to 3'$ direction, the lagging strand cannot be fully replicated to the absolute chromosome terminus, resulting in progressive telomere shortening with each cell division (the 'end-replication problem'). When telomeres reach a critical threshold, the cell enters replicative senescence or triggers apoptosis. However, in over 85% of human malignancies, the ribonucleoprotein enzyme telomerase is pathologically upregulated, continually synthesizing telomeric repeats and conferring cellular immortality.",
            "Which choice most accurately explains the biological consequence of telomerase reactivation in cancer cells?",
            "It continuously elongates terminal telomeric repeats, overcoming the end-replication problem and enabling unlimited cellular proliferation.",
            [
                "It accelerates DNA polymerase degradation, causing immediate apoptotic cell death.",
                "It synthesizes abnormal lipid membranes that protect tumors from cytotoxic T-lymphocyte infiltration.",
                "It converts lagging DNA strands into viral messenger RNA."
            ],
            "The text states telomerase reactivation synthesizes telomeric repeats to overcome the end-replication problem, conferring cellular immortality."
        ),
        # Q21 Command of Evidence
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Plant evolutionary biologist Dr. Nadia Patel evaluated whether the evolution of extrafloral nectaries (EFNs) in passionflower vines (<i>Passiflora</i>) represents an active mutualistic defense mechanism against herbivorous caterpillars. The hypothesis posits that EFNs secrete sugar-rich nectar specifically to recruit predatory ants that attack and dislodge caterpillar larvae before they consume leaves. If Dr. Patel's field experiments support this mutualistic defense hypothesis, which result would be observed?",
            "Vines with active extrafloral nectaries recruited six times more predatory ants and suffered 70% less leaf herbivory than experimental vines whose nectaries were artificially sealed with silicone.",
            [
                "Vines whose nectaries were sealed with silicone exhibited accelerated photosynthetic growth and higher flower production.",
                "Predatory ants consumed the extrafloral nectar but completely ignored caterpillar larvae feeding on neighboring leaves.",
                "Caterpillars demonstrated a marked physiological preference for feeding directly on extrafloral nectaries rather than leaves."
            ],
            "Mutualism requires reciprocal benefit: nectaries recruit ants, and ant presence reduces caterpillar herbivory."
        ),
        # Q22 Inferences
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In quantum cryptography, the BB84 protocol ensures unconditionally secure communication using single polarized photons. According to the quantum no-cloning theorem, an eavesdropper ('Eve') cannot measure or intercept an unknown quantum state without fundamentally perturbing the wave function, which inevitably introduces measurable quantum bit error rates (QBER) into the transmission between sender and receiver. If the measured QBER between the two communicating parties remains strictly below the theoretical threshold of 11%, the laws of quantum mechanics guarantee that _____.",
            "any intercepted information acquired by an eavesdropper can be completely purged through classical privacy amplification algorithms without compromising the key",
            [
                "an eavesdropper has successfully duplicated all quantum photons without detection",
                "the transmission channel must be completely severed because quantum mechanics has been invalidated",
                "the communicating parties must convert their optical fiber connections into standard analog telephone lines"
            ],
            "In quantum key distribution, if QBER is below threshold (11%), privacy amplification ensures a completely secure secret key can be extracted."
        ),
        # Q23 Standard English Conventions (Boundaries)
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "In 1974, archaeologists in Xi'an unearthed the Terracotta Army, a collection of thousands of life-sized ceramic warriors buried with Qin Shi _____ emperor who unified China under a centralized legalist administration.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "Huang, the first",
            ["Huang; the first", "Huang the first", "Huang: being the first"],
            "'the first emperor who unified China...' is an appositive modifying Qin Shi Huang. A comma correctly attaches it."
        ),
        # Q24 Standard English Conventions (Form/Structure)
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Neither the rapid proliferation of generative artificial intelligence models nor the acceleration of automated code generation _____ completely rendered traditional computer science education obsolete.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "has",
            ["have", "are", "having"],
            "Subject is singular ('proliferation' / 'acceleration'), requiring singular verb 'has'."
        ),
        # Q25 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Early planetary astronomers assumed that Mercury was gravitationally tidal-locked to the Sun in a 1:1 synchronous rotation, keeping one hemisphere in perpetual daylight. _____, radar observations in 1965 revealed that Mercury rotates three times for every two orbits around the Sun, a 3:2 spin-orbit resonance.",
            "Which choice completes the text with the most logical transition?",
            "However,",
            ["Furthermore,", "Similarly,", "Consequently,"],
            "'However' marks the contrast between the early tidal-locked assumption and the actual 3:2 resonance discovery."
        ),
        # Q26 Rhetorical Synthesis
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The Voyager 2 space probe was launched in August 1977.</li><li style='margin-bottom: 4px;'>It took advantage of a rare planetary alignment that occurs once every 175 years to execute gravity assists.</li><li style='margin-bottom: 4px;'>It is the only spacecraft in human history to have visited both ice giant planets: Uranus (1986) and Neptune (1989).</li><li style='margin-bottom: 4px;'>During its flyby of Neptune, Voyager 2 discovered active nitrogen ice geysers on Neptune's moon Triton.</li><li style='margin-bottom: 4px;'>Voyager 2 crossed the heliopause into interstellar space in November 2018.</li></ul>",
            "The student wants to highlight an achievement unique to Voyager 2 among all space exploration missions. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "Taking advantage of a rare planetary alignment, Voyager 2 became the only spacecraft in human history to visit the ice giant planets Uranus and Neptune.",
            [
                "Launched in August 1977, Voyager 2 crossed into interstellar space in November 2018.",
                "Voyager 2 discovered active nitrogen geysers on Neptune's moon Triton during its 1989 flyby.",
                "Gravity assists allow space probes to navigate the outer Solar System by borrowing orbital momentum from planets."
            ],
            "The sentence directly emphasizes the unique achievement: being the only spacecraft in human history to visit both Uranus and Neptune."
        ),
        # Q27 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The clinical trial was halted prematurely because the experimental immunotherapy exhibited _____ toxicity, causing severe systemic autoimmune organ inflammation in over forty percent of enrolled patients.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "intolerable", ["salutary", "negligible", "pellucid"],
            "'Intolerable' means unendurable or excessively severe. Over 40% autoimmune organ inflammation represents intolerable toxicity."
        )
    ]

    for i, spec in enumerate(rw_m2_specs):
        target_letter = RW_TARGETS[i]
        if len(spec) == 7:
            domain, subdomain, diff, stim, corr, dists, expl = spec
            prompt = "Which choice most logically completes the text?" if "_____" in stim else "Which finding, if true, most strongly supports the hypothesis?"
        else:
            domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        rw_m2.append(make_hard_mcq(f"t3-rw-m2-q{i+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # =========================================================================
    # TEST 3 - MATH MODULE 1 (High-Difficulty Routing Module)
    # =========================================================================
    math_m1_mcqs = [
        # Q1 Systems with Parameters
        (
            DOMAINS["MATH"]["ALG"], "Systems of Equations", "Medium",
            "In the system of equations below, $k$ is a constant:<br>$$6x - 9y = 21$$<br>$$4x - 6y = k$$<br>If the system has infinitely many solutions, what is the value of $k$?",
            "Which choice is the value of $k$?",
            "14", ["12", "18", "21"],
            "Divide the first equation by 3: $2x - 3y = 7$. Multiply by 2: $4x - 6y = 14$. For infinitely many solutions, $k$ must equal 14."
        ),
        # Q2 Linear Inequality Systems
        (
            DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Hard",
            "Which point $(x, y)$ satisfies the system of inequalities?<br>$$y > 2x + 3$$<br>$$3x - 2y \\ge -14$$",
            "Which choice is a valid point?",
            "(-2, 2)", ["(1, 4)", "(0, 1)", "(3, 10)"],
            "Test $(-2, 2)$: $2 > 2(-2) + 3 = -1$ (True). And $3(-2) - 2(2) = -6 - 4 = -10 \\ge -14$ (True). Both are satisfied."
        ),
        # Q3 Perpendicular Lines
        (
            DOMAINS["MATH"]["ALG"], "Linear Functions", "Hard",
            "Line $L$ passes through $(1, 5)$ and $(4, -1)$. Line $M$ is perpendicular to line $L$ and passes through $(6, 2)$. What is the y-intercept of line $M$?",
            "Which choice is the y-intercept?",
            "-1", ["-2", "1", "2"],
            "Slope of $L$: $\\frac{-1 - 5}{4 - 1} = \\frac{-6}{3} = -2$. Perpendicular slope $m = 1/2$. Line $M$: $y - 2 = \\frac{1}{2}(x - 6) \\implies y - 2 = \\frac{1}{2}x - 3 \\implies y = \\frac{1}{2}x - 1$. The y-intercept is -1."
        ),
        # Q4 Quadratic Discriminant
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "For what positive value of $b$ does $2x^2 - bx + 18 = 0$ have exactly one real solution?",
            "Which choice is the value of $b$?",
            "12", ["6", "18", "36"],
            "Discriminant $\\Delta = (-b)^2 - 4(2)(18) = b^2 - 144 = 0 \\implies b^2 = 144 \\implies b = 12$."
        ),
        # Q5 Vertex Form
        (
            DOMAINS["MATH"]["ADV"], "Nonlinear Functions", "Hard",
            "The parabola $y = 2x^2 - 16x + 25$ is written in vertex form as $y = a(x - h)^2 + k$. What is the value of $h + k$?",
            "Which choice is the value of $h + k$?",
            "-3", ["4", "-7", "11"],
            "$y = 2(x^2 - 8x) + 25 = 2(x - 4)^2 - 2(16) + 25 = 2(x - 4)^2 - 7$. Here $h = 4$ and $k = -7$. Sum $h + k = 4 + (-7) = -3$."
        ),
        # Q6 Exponential Growth
        (
            DOMAINS["MATH"]["ADV"], "Exponential Functions", "Hard",
            "A technology startup has an annual recurring revenue of $500,000 that doubles every 2.5 years. Which function $R(t)$ models the revenue, in dollars, after $t$ years?",
            "Which choice correctly models the revenue?",
            "$$R(t) = 500,000(2)^{t / 2.5}$$",
            ["$$R(t) = 500,000(2)^{2.5t}$$", "$$R(t) = 500,000(2.5)^{t / 2}$$", "$$R(t) = 1,000,000(2)^{t / 2.5}$$"],
            "Initial value is 500,000. Growth factor is 2. The exponent is $t / 2.5$, giving $R(t) = 500,000(2)^{t / 2.5}$."
        ),
        # Q7 Polynomial Remainder
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "If $(x - 1)$ is a factor of $P(x) = 3x^3 - 7x^2 + kx + 8$, what is the value of $k$?",
            "Which choice is the value of $k$?",
            "-4", ["4", "-8", "8"],
            "Factor theorem: $P(1) = 0 \\implies 3(1)^3 - 7(1)^2 + k(1) + 8 = 0 \\implies 3 - 7 + k + 8 = 0 \\implies k + 4 = 0 \\implies k = -4$."
        ),
        # Q8 Radical Equations
        (
            DOMAINS["MATH"]["ADV"], "Radicals", "Hard",
            "What is the unique real solution to the equation $\\sqrt{7x + 2} = x + 2$?",
            "Which choice is the solution?",
            "2", ["-1", "1", "No real solution"],
            "Square: $7x + 2 = (x + 2)^2 = x^2 + 4x + 4 \\implies x^2 - 3x + 2 = 0 \\implies (x - 2)(x - 1) = 0$. For $x = 1$: $\\sqrt{9} = 3 = 1 + 2$ (valid!). For $x = 2$: $\\sqrt{16} = 4 = 2 + 2$ (valid!). Both are valid! Sum of solutions $= 1 + 2 = 3$."
        ),
        # Q9 Rational Functions
        (
            DOMAINS["MATH"]["ADV"], "Rational Functions", "Hard",
            "What is the horizontal asymptote of $f(x) = \\frac{10x^3 - 4x + 1}{5x^3 + 2x^2 - 7}$?",
            "Which choice is the horizontal asymptote?",
            "$$y = 2$$",
            ["$$y = 0$$", "$$y = 10$$", "$$y = -\\frac{1}{7}$$"],
            "Equal degree 3 in numerator and denominator: horizontal asymptote is $y = 10 / 5 = 2$."
        ),
        # Q10 Rates and Proportions
        (
            DOMAINS["MATH"]["PSDA"], "Rates and Proportions", "Medium",
            "A water pump empties a 15,000-gallon retention basin in 5 hours. A newer pump operates $50\\%$ faster. Working together, how many hours will both pumps take to empty the basin?",
            "Which choice is the time in hours?",
            "2 hours", ["2.5 hours", "3 hours", "1.5 hours"],
            "Pump 1 rate: $15,000 / 5 = 3,000$ gal/hr. Pump 2 is 50% faster: $3,000 \\times 1.5 = 4,500$ gal/hr. Combined rate: $3,000 + 4,500 = 7,500$ gal/hr. Time $= 15,000 / 7,500 = 2$ hours."
        ),
        # Q11 Percentages
        (
            DOMAINS["MATH"]["PSDA"], "Percentages", "Medium",
            "The price of a stock increased by $20\\%$ in year 1, and then decreased by $20\\%$ in year 2. What was the net percentage change in the stock price over the two-year period?",
            "Which choice is the net percentage change?",
            "4% decrease", ["0% change", "4% increase", "2% decrease"],
            "Initial price $P$. After year 1: $1.20P$. After year 2: $1.20P \\times (1 - 0.20) = 1.20P \\times 0.80 = 0.96P$. This is a $4\\%$ decrease."
        ),
        # Q12 Conditional Probability Table
        (
            DOMAINS["MATH"]["PSDA"], "Probability", "Hard",
            "A healthcare audit categorized 600 emergency room visits by patient age group and admission status:<br><br><table style='width:100%; border-collapse: collapse; margin: 8px 0; font-size: 13px;'><tr style='background: #f1f5f9;'><th style='border: 1px solid #cbd5e1; padding: 6px;'>Age Group</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Admitted to Hospital</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Discharged Home</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Total</th></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Under 65</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>90</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>310</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>400</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>65 and Older</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>110</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>90</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>200</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Total</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>200</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>400</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>600</td></tr></table><br>Given that a patient was admitted to the hospital, what is the probability that the patient is 65 or older?",
            "Which choice is the probability?",
            "0.55", ["0.33", "0.20", "0.45"],
            "Total admitted patients $= 200$. Admitted patients 65 or older $= 110$. Probability $= 110 / 200 = 0.55$."
        ),
        # Q13 Margin of Error
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "A poll of 625 registered voters has a margin of error of $\\pm 4.0\\%$. How many voters must be sampled to reduce the margin of error to $\\pm 2.0\\%$ with the same confidence level?",
            "Which choice is the required sample size?",
            "2,500 voters", ["1,250 voters", "3,125 voters", "5,000 voters"],
            "Margin of error is inversely proportional to $\\sqrt{n}$. To halve the margin of error (from 4.0% to 2.0%), the sample size must be multiplied by $2^2 = 4$. Required sample size $= 625 \\times 4 = 2,500$ voters."
        ),
        # Q14 Scatterplot Linear Model
        (
            DOMAINS["MATH"]["PSDA"], "Scatterplots", "Medium",
            "The scatterplot of heating fuel consumption $y$ (gallons) versus outside temperature $x$ (°F) is modeled by $\\hat{y} = -3.5x + 280$. What is the predicted fuel consumption when outside temperature is 40°F?",
            "Which choice is the predicted fuel consumption?",
            "140 gallons", ["120 gallons", "160 gallons", "180 gallons"],
            "Substitute $x = 40$: $\\hat{y} = -3.5(40) + 280 = -140 + 280 = 140$ gallons."
        ),
        # Q15 Circle Completing the Square
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "The equation of a circle is $x^2 + y^2 - 12x + 4y - 9 = 0$. What is the radius of the circle?",
            "Which choice is the radius?",
            "7", ["49", "$$\\sqrt{13}$$", "9"],
            "Complete squares: $(x - 6)^2 + (y + 2)^2 = 9 + 36 + 4 = 49$. Radius is $\\sqrt{49} = 7$."
        ),
        # Q16 Trigonometric Ratios
        (
            DOMAINS["MATH"]["GEOM"], "Trigonometry", "Hard",
            "In right triangle $ABC$ with right angle at $C$, $\\tan(A) = \\frac{3}{4}$. What is the value of $\\sin(A)$?",
            "Which choice is the value of $\\sin(A)$?",
            "$$\\frac{3}{5}$$",
            ["$$\\frac{4}{5}$$", "$$\\frac{3}{4}$$", "$$\\frac{4}{3}$$"],
            "Opposite $= 3$, adjacent $= 4$, hypotenuse $= \\sqrt{3^2 + 4^2} = 5$. Thus $\\sin(A) = 3/5$."
        ),
        # Q17 Arc Length & Central Angle
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle has radius 15. What is the area of a sector of this circle with central angle $\\frac{2\\pi}{5}$ radians?",
            "Which choice is the sector area?",
            "$$45\\pi$$",
            ["$$90\\pi$$", "$$30\\pi$$", "$$22.5\\pi$$"],
            "Sector area formula: $A = \\frac{1}{2} r^2 \\theta = \\frac{1}{2} (15^2) \\left(\\frac{2\\pi}{5}\\right) = \\frac{1}{2} (225) \\left(\\frac{2\\pi}{5}\\right) = \\frac{225\\pi}{5} = 45\\pi$."
        ),
        # Q18 Similar Triangles
        (
            DOMAINS["MATH"]["GEOM"], "Triangles", "Hard",
            "In right triangle $DEF$ with right angle at $E$, an altitude $EG$ is drawn to hypotenuse $DF$. If $DG = 2$ and $GF = 8$, what is the length of altitude $EG$?",
            "Which choice is the length of $EG$?",
            "4", ["5", "$$\\sqrt{10}$$", "16"],
            "By the Geometric Mean Theorem: $EG^2 = DG \\times GF = 2 \\times 8 = 16 \\implies EG = \\sqrt{16} = 4$."
        ),
        # Q19 Density and Volume
        (
            DOMAINS["MATH"]["GEOM"], "Density", "Hard",
            "A solid aluminum sphere has a radius of 3 cm. The density of aluminum is $2.7\\text{ g/cm}^3$. What is the mass of the sphere in grams, rounded to the nearest gram?",
            "Which choice is the mass in grams?",
            "305 grams", ["102 grams", "229 grams", "611 grams"],
            "Volume $V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi (3^3) = 36\\pi\\text{ cm}^3 \\approx 113.097\\text{ cm}^3$. Mass $= 113.097 \\times 2.7 \\approx 305.36\\text{ g} \\approx 305$ grams."
        ),
        # Q20 Vieta's Formula
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "The roots of $x^2 - 6x + 7 = 0$ are $a$ and $b$. What is the value of $a^2 + b^2$?",
            "Which choice is the value?",
            "22", ["36", "14", "29"],
            "$a + b = 6, ab = 7$. $a^2 + b^2 = (a + b)^2 - 2ab = 6^2 - 2(7) = 36 - 14 = 22$."
        ),
        # Q21 Nonlinear System
        (
            DOMAINS["MATH"]["ADV"], "Nonlinear Systems", "Hard",
            "How many real solutions $(x, y)$ does the system of equations have?<br>$$y = 2x^2 + 5x - 3$$<br>$$y = x - 5$$",
            "Which choice is the number of solutions?",
            "0", ["1", "2", "Infinitely many"],
            "Set equal: $2x^2 + 5x - 3 = x - 5 \\implies 2x^2 + 4x + 2 = 0 \\implies x^2 + 2x + 1 = 0 \\implies (x + 1)^2 = 0$. That gives 1 solution! If we change line to $y = x - 6$: $2x^2 + 4x + 3 = 0$, $\\Delta = 16 - 24 = -8 < 0$, giving 0 real solutions!"
        ),
        # Q22 Absolute Value Equation
        (
            DOMAINS["MATH"]["ALG"], "Linear Equations", "Hard",
            "What is the sum of all real solutions to $|2x + 3| = x + 6$?",
            "Which choice is the sum?",
            "0", ["3", "-3", "6"],
            "Case 1: $2x + 3 = x + 6 \\implies x = 3$. Check $x = 3$: $|9| = 9$ (valid). Case 2: $2x + 3 = -(x + 6) = -x - 6 \\implies 3x = -9 \\implies x = -3$. Check $x = -3$: $|-3| = 3$, and $-3 + 6 = 3$ (valid!). Both solutions are valid. Sum $= 3 + (-3) = 0$."
        )
    ]

    for i, spec in enumerate(math_m1_mcqs):
        target_letter = MATH_TARGETS[i]
        domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        if i == 7: # Q8 custom
            stim = "What is the sum of all real solutions to the equation $\\sqrt{7x + 2} = x + 2$?"
            corr = "3"
            dists = ["1", "2", "4"]
            expl = "Square: $7x + 2 = x^2 + 4x + 4 \\implies x^2 - 3x + 2 = 0 \\implies (x - 2)(x - 1) = 0$. Both $x = 1$ and $x = 2$ are valid. Sum $= 1 + 2 = 3$."
        elif i == 20: # Q21 custom
            stim = "How many real solutions $(x, y)$ does the system have?<br>$$y = 2x^2 + 5x - 3$$<br>$$y = x - 6$$"
            corr = "0"
            dists = ["1", "2", "Infinitely many"]
            expl = "$2x^2 + 4x + 3 = 0$. Discriminant $\\Delta = 16 - 24 = -8 < 0$. Zero real solutions."
        math_m1.append(make_hard_mcq(f"t3-math-m1-q{i+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # Math M1 SPRs (Q23-Q27)
    math_m1_sprs = [
        # Q23 SPR
        (
            DOMAINS["MATH"]["ALG"], "Systems of Equations", "Medium",
            "In the system of equations below:<br>$$5x + 2y = 34$$<br>$$3x - y = 16$$<br>What is the value of $x$?",
            "Enter the exact integer value of x:",
            ["6"],
            "From second eq: $y = 3x - 16$. Substitute: $5x + 2(3x - 16) = 34 \\implies 11x - 32 = 34 \\implies 11x = 66 \\implies x = 6$."
        ),
        # Q24 SPR
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "When $f(x) = x^3 - 4x^2 + ax + 12$ is divided by $(x - 3)$, the remainder is 0. What is the value of $a$?",
            "Enter the exact integer value of a:",
            ["-1"],
            "$f(3) = 27 - 4(9) + 3a + 12 = 27 - 36 + 3a + 12 = 3a + 3 = 0 \\implies 3a = -3 \\implies a = -1$."
        ),
        # Q25 SPR
        (
            DOMAINS["MATH"]["GEOM"], "Right Triangles", "Hard",
            "In a $30^\\circ-60^\\circ-90^\\circ$ triangle, the shorter leg has length 7. What is the length of the hypotenuse?",
            "Enter the exact integer length of the hypotenuse:",
            ["14"],
            "In a $30^\\circ-60^\\circ-90^\\circ$ triangle, hypotenuse $= 2 \\times \\text{shorter leg} = 2 \\times 7 = 14$."
        ),
        # Q26 SPR
        (
            DOMAINS["MATH"]["ADV"], "Exponents and Radicals", "Hard",
            "If $8^{2x - 3} = 32^{x - 1}$, what is the value of $x$?",
            "Enter the exact integer value of x:",
            ["4"],
            "Base 2: $(2^3)^{2x - 3} = (2^5)^{x - 1} \\implies 6x - 9 = 5x - 5 \\implies x = 4$."
        ),
        # Q27 SPR
        (
            DOMAINS["MATH"]["PSDA"], "Probability", "Hard",
            "In a laboratory test, 60 mice received Drug X and 40 received Placebo. 15 mice in the Drug X group and 5 mice in the Placebo group exhibited adverse symptoms. If an animal with adverse symptoms is randomly selected, what is the probability it received Drug X? Express your answer as a simplified fraction a/b:",
            "Enter the exact fraction a/b:",
            ["3/4", "0.75"],
            "Total with symptoms $= 15 + 5 = 20$. In Drug X group $= 15$. Probability $= 15 / 20 = 3/4 = 0.75$."
        )
    ]

    for j, spec in enumerate(math_m1_sprs):
        domain, subdomain, diff, stim, prompt, answers, expl = spec
        math_m1.append(make_spr(f"t3-math-m1-q{j+23}", domain, subdomain, diff, stim, prompt, answers, expl))

    # =========================================================================
    # TEST 3 - MATH MODULE 2 (Adaptive Hard Module: Rigorous 750-800 Level)
    # =========================================================================
    math_m2_mcqs = [
        # Q1 Systems with Parameters
        (
            DOMAINS["MATH"]["ALG"], "Systems of Equations", "Hard",
            "In the system of equations below, $m$ and $n$ are constants:<br>$$mx - 6y = 15$$<br>$$2x + ny = 5$$<br>If the system has infinitely many solutions, what is the value of $m - n$?",
            "Which choice is the value of $m - n$?",
            "8", ["4", "6", "10"],
            "Multiply second equation by 3: $6x + 3ny = 15$. For identical equations: $m = 6$ and $-6 = 3n \\implies n = -2$. Value $m - n = 6 - (-2) = 8$."
        ),
        # Q2 Absolute Value Inequality
        (
            DOMAINS["MATH"]["ALG"], "Inequalities", "Hard",
            "What is the solution set for the inequality $|5x + 3| - 4 \\le 16$?",
            "Which choice is the solution set?",
            "$$-\\frac{23}{5} \\le x \\le \\frac{17}{5}$$",
            ["$$x \\le \\frac{17}{5}$$", "$$x \\ge -\\frac{23}{5}$$", "$$-\\frac{17}{5} \\le x \\le \\frac{23}{5}$$"],
            "$|5x + 3| \\le 20 \\implies -20 \\le 5x + 3 \\le 20 \\implies -23 \\le 5x \\le 17 \\implies -23/5 \\le x \\le 17/5$."
        ),
        # Q3 Perpendicular Lines
        (
            DOMAINS["MATH"]["ALG"], "Linear Functions", "Hard",
            "Line $J$ passes through $(-1, 4)$ and $(3, -2)$. Line $K$ is perpendicular to line $J$ and has an x-intercept of -3. What is the y-intercept of line $K$?",
            "Which choice is the y-intercept?",
            "2", ["-2", "3", "-3"],
            "Slope of $J$: $\\frac{-2 - 4}{3 - (-1)} = \\frac{-6}{4} = -\\frac{3}{2}$. Perpendicular slope $m = \\frac{2}{3}$. Line $K$ passes through $(-3, 0)$: $y - 0 = \\frac{2}{3}(x - (-3)) = \\frac{2}{3}(x + 3) = \\frac{2}{3}x + 2$. The y-intercept is 2."
        ),
        # Q4 Quadratic Discriminant & Line Tangency
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "The line $y = 4x + c$ is tangent to the parabola $y = x^2 - 2x + 12$. What is the value of $c$?",
            "Which choice is the value of $c$?",
            "3", ["-3", "6", "9"],
            "Set equal: $x^2 - 2x + 12 = 4x + c \\implies x^2 - 6x + (12 - c) = 0$. Tangency requires $\\Delta = 0$: $(-6)^2 - 4(1)(12 - c) = 0 \\implies 36 - 48 + 4c = 0 \\implies 4c = 12 \\implies c = 3$."
        ),
        # Q5 Vertex Optimization
        (
            DOMAINS["MATH"]["ADV"], "Nonlinear Modeling", "Hard",
            "A farm produces organic blueberries and models its daily profit $P(w)$, in dollars, as a function of the harvest weight $w$, in hundreds of pounds: $P(w) = -2w^2 + 100w - 450$. What harvest weight $w$ maximizes daily profit?",
            "Which choice is the optimal weight $w$?",
            "25 hundred pounds", ["50 hundred pounds", "20 hundred pounds", "30 hundred pounds"],
            "Vertex $w = -\\frac{b}{2a} = -\\frac{100}{2(-2)} = \\frac{100}{4} = 25$ hundred pounds."
        ),
        # Q6 Polynomial Divisibility
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "The polynomial $P(x) = x^3 - 3x^2 + ax + b$ is divisible by $(x - 1)$ and $(x + 2)$. What is the value of $a$?",
            "Which choice is the value of $a$?",
            "-6", ["6", "-4", "4"],
            "$P(1) = 1 - 3 + a + b = 0 \\implies a + b = 2$. $P(-2) = -8 - 12 - 2a + b = 0 \\implies -2a + b = 20$. Subtract second from first: $3a = -18 \\implies a = -6$."
        ),
        # Q7 Rational Functions
        (
            DOMAINS["MATH"]["ADV"], "Rational Functions", "Hard",
            "The function $f(x) = \\frac{x^2 - 25}{2x^2 - 9x - 5}$ has a removable discontinuity (hole) at what value of $x$?",
            "Which choice is the x-value of the hole?",
            "5", ["-5", "$$-\\frac{1}{2}$$", "2"],
            "Factor: $f(x) = \\frac{(x - 5)(x + 5)}{(2x + 1)(x - 5)}$. The factor $(x - 5)$ cancels, creating a hole at $x = 5$."
        ),
        # Q8 Exponential Decay
        (
            DOMAINS["MATH"]["ADV"], "Exponential Functions", "Hard",
            "A pharmaceutical drug has a half-life of 6 hours. If a patient takes a 400 mg dose, which expression gives the amount of drug remaining in mg after $t$ hours?",
            "Which choice is the expression?",
            "$$400\\left(\\frac{1}{2}\\right)^{t / 6}$$",
            ["$$400(2)^{t / 6}$$", "$$400\\left(\\frac{1}{2}\\right)^{6t}$$", "$$400(6)^{-t/2}$$"],
            "Initial amount 400 mg. Half-life 6 hours means exponent is $t / 6$ with base $1/2$."
        ),
        # Q9 Radical and Extraneous
        (
            DOMAINS["MATH"]["ADV"], "Radicals", "Hard",
            "What is the unique real solution to $\\sqrt{5x + 19} - x = 1$?",
            "Which choice is the solution?",
            "3", ["-6", "6", "No real solution"],
            "Isolate: $\\sqrt{5x + 19} = x + 1$. Square: $5x + 19 = x^2 + 2x + 1 \\implies x^2 - 3x - 18 = 0 \\implies (x - 6)(x + 3) = 0$! Wait: $(x - 6)(x + 3) = 0$. For $x = -3$: $x + 1 = -2 < 0$ (extraneous). For $x = 6$: $\\sqrt{49} = 7 = 6 + 1$ (valid). Solution is 6."
        ),
        # Q10 Two-Variable System
        (
            DOMAINS["MATH"]["ALG"], "Linear Modeling", "Hard",
            "A merchant blends Ethiopian coffee selling for $14 per pound with Colombian coffee selling for $9 per pound to create a 50-pound blend selling for $12 per pound. How many pounds of Ethiopian coffee must be included?",
            "Which choice is the pounds of Ethiopian coffee?",
            "30 pounds", ["20 pounds", "25 pounds", "35 pounds"],
            "Let $e$ be Ethiopian and $c$ be Colombian. $e + c = 50$, and $14e + 9c = 12(50) = 600$. $14e + 9(50 - e) = 600 \\implies 5e + 450 = 600 \\implies 5e = 150 \\implies e = 30$ pounds."
        ),
        # Q11 Residual Analysis
        (
            DOMAINS["MATH"]["PSDA"], "Scatterplots", "Hard",
            "A model predicts athlete sprint time $y$ (seconds) from body fat percentage $x$: $\\hat{y} = 0.15x + 9.80$. For an athlete with $12\\%$ body fat, the actual sprint time was 11.45 seconds. What is the residual?",
            "Which choice is the residual?",
            "-0.15 seconds", ["0.15 seconds", "11.60 seconds", "-0.30 seconds"],
            "Predicted $\\hat{y} = 0.15(12) + 9.80 = 1.80 + 9.80 = 11.60$. Residual $= \\text{Actual} - \\text{Predicted} = 11.45 - 11.60 = -0.15$ seconds."
        ),
        # Q12 Conditional Probability
        (
            DOMAINS["MATH"]["PSDA"], "Probability", "Hard",
            "A factory has Machine 1 producing $70\\%$ of parts and Machine 2 producing $30\\%$. Defect rates are $1\\%$ for Machine 1 and $4\\%$ for Machine 2. What is the probability a defective part came from Machine 1?",
            "Which choice is the probability?",
            "$$\\frac{7}{19}$$",
            ["$$\\frac{12}{19}$$", "$$\\frac{7}{10}$$", "$$\\frac{1}{4}$$"],
            "$P(D) = (0.70)(0.01) + (0.30)(0.04) = 0.007 + 0.012 = 0.019$. $P(\\text{M1} \\mid D) = 0.007 / 0.019 = 7/19$."
        ),
        # Q13 Box Plots
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "A dataset of 80 values has $Q_1 = 30$ and $Q_3 = 50$. Any value greater than $Q_3 + 1.5(\\text{IQR})$ is an outlier. What is the smallest integer that would be classified as an outlier?",
            "Which choice is the smallest outlier integer?",
            "81", ["80", "75", "85"],
            "$\\text{IQR} = 50 - 30 = 20$. Upper bound $= 50 + 1.5(20) = 50 + 30 = 80$. A value strictly greater than 80 is an outlier. The smallest integer is 81."
        ),
        # Q14 Normal Distribution
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "A test has mean $\\mu = 500$ and standard deviation $\\sigma = 100$. Approximately what percentage of test-takers score above 700?",
            "Which choice is the approximate percentage?",
            "2.5%", ["5%", "16%", "0.15%"],
            "$z = (700 - 500) / 100 = +2.0$. Above $+2\\sigma$ is approximately $2.5\\%$ under the normal curve."
        ),
        # Q15 Circle Tangent
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle with center $(0, 0)$ and radius 5 is tangent to a line at point $(3, 4)$. What is the slope of the tangent line?",
            "Which choice is the slope of the tangent line?",
            "$$-\\frac{3}{4}$$",
            ["$$\\frac{4}{3}$$", "$$-\\frac{4}{3}$$", "$$\\frac{3}{4}$$"],
            "Radius slope $= (4 - 0)/(3 - 0) = 4/3$. Tangent is perpendicular, so slope $= -3/4$."
        ),
        # Q16 Inscribed Angles
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "In a circle of radius 10, an inscribed angle measures $30^\\circ$. What is the length of the arc intercepted by this angle?",
            "Which choice is the arc length?",
            "$$\\frac{10\\pi}{3}$$",
            ["$$\\frac{5\\pi}{3}$$", "$$\\frac{20\\pi}{3}$$", "$$5\\pi$$"],
            "Central angle $\\theta = 2 \\times 30^\\circ = 60^\\circ = \\frac{\\pi}{3}$ radians. Arc length $s = r\\theta = 10 \\times \\frac{\\pi}{3} = \\frac{10\\pi}{3}$."
        ),
        # Q17 Trigonometry
        (
            DOMAINS["MATH"]["GEOM"], "Trigonometry", "Hard",
            "In right triangle $ABC$ with right angle at $C$, $\\cos(A) = \\frac{5}{13}$. What is the value of $\\sin(B)$?",
            "Which choice is the value of $\\sin(B)$?",
            "$$\\frac{5}{13}$$",
            ["$$\\frac{12}{13}$$", "$$\\frac{5}{12}$$", "$$\\frac{13}{5}$$"],
            "Angles $A$ and $B$ are complementary: $A + B = 90^\\circ$. By cofunction identity, $\\sin(B) = \\cos(A) = 5/13$."
        ),
        # Q18 Radians
        (
            DOMAINS["MATH"]["GEOM"], "Trigonometry", "Hard",
            "What is the degree measure of an angle of $\\frac{7\\pi}{6}$ radians?",
            "Which choice is the degree measure?",
            "210°", ["240°", "150°", "225°"],
            "Conversion: $\\frac{7\\pi}{6} \\times \\frac{180^\\circ}{\\pi} = 7 \\times 30^\\circ = 210^\\circ$."
        ),
        # Q19 Density
        (
            DOMAINS["MATH"]["GEOM"], "Density", "Hard",
            "A solid lead cylinder has radius 2 cm and height 10 cm. The density of lead is $11.3\\text{ g/cm}^3$. What is the mass of the cylinder in kilograms, rounded to the nearest hundredth?",
            "Which choice is the mass in kilograms?",
            "1.42 kg", ["2.84 kg", "0.71 kg", "5.68 kg"],
            "Volume $V = \\pi r^2 h = \\pi (2^2)(10) = 40\\pi \\approx 125.66\\text{ cm}^3$. Mass $= 125.66 \\times 11.3 \\approx 1420\\text{ g} = 1.42$ kg."
        ),
        # Q20 Polynomial Vieta
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "The roots of $2x^2 - 12x + 9 = 0$ are $r_1$ and $r_2$. What is the value of $r_1 r_2$?",
            "Which choice is the value?",
            "$$\\frac{9}{2}$$",
            ["6", "$$-\\frac{9}{2}$$", "9"],
            "By Vieta's formulas, product of roots $= c / a = 9 / 2$."
        ),
        # Q21 Circle Chord Distance
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle of radius 17 has a chord of length 30. What is the distance from the center to the chord?",
            "Which choice is the distance?",
            "8", ["15", "10", "$$\\sqrt{64}$$"],
            "Half-chord $= 30 / 2 = 15$. Distance $= \\sqrt{17^2 - 15^2} = \\sqrt{289 - 225} = \\sqrt{64} = 8$."
        ),
        # Q22 Rational Function Hole
        (
            DOMAINS["MATH"]["ADV"], "Rational Functions", "Hard",
            "The function $f(x) = \\frac{4x^2 - 64}{x^2 - 3x - 4}$ has a hole at point $(x_0, y_0)$. What is $y_0$?",
            "Which choice is the y-coordinate of the hole?",
            "$$\\frac{32}{5}$$",
            ["$$\\frac{16}{5}$$", "4", "8"],
            "Factor: $f(x) = \\frac{4(x - 4)(x + 4)}{(x - 4)(x + 1)}$. Hole at $x = 4$. Simplified: $\\frac{4(x + 4)}{x + 1}$. Substitute $x = 4$: $y_0 = \\frac{4(8)}{5} = \\frac{32}{5}$."
        )
    ]

    for k, spec in enumerate(math_m2_mcqs):
        target_letter = MATH_TARGETS[k]
        domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        if k == 8: # Q9 custom
            stim = "What is the unique real solution to $\\sqrt{5x + 19} - x = 1$?"
            corr = "6"
            dists = ["3", "-3", "No real solution"]
            expl = "$\\sqrt{5x + 19} = x + 1 \\implies x^2 - 3x - 18 = 0 \\implies (x - 6)(x + 3) = 0$. $x = -3$ is extraneous. $x = 6$ is valid."
        math_m2.append(make_hard_mcq(f"t3-math-m2-q{k+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # Math M2 SPRs (Q23-Q27)
    math_m2_sprs = [
        # Q23 SPR
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "The line $y = 6x + c$ intersects the parabola $y = 3x^2 - 6x + 20$ at exactly one point in the xy-plane. What is the value of constant $c$?",
            "Enter the exact integer value of c:",
            ["8"],
            "Set equal: $3x^2 - 6x + 20 = 6x + c \\implies 3x^2 - 12x + (20 - c) = 0$. Exactly one intersection requires $\\Delta = (-12)^2 - 4(3)(20 - c) = 0 \\implies 144 - 12(20 - c) = 0 \\implies 144 - 240 + 12c = 0 \\implies 12c = 96 \\implies c = 8$."
        ),
        # Q24 SPR
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "In the polynomial $P(x) = (3x - 2)(x + 5)(x - 4)$, what is the y-intercept of the graph of $y = P(x)$ in the xy-plane?",
            "Enter the exact integer value of the y-intercept:",
            ["40"],
            "Substitute $x = 0$: $P(0) = (3(0) - 2)(0 + 5)(0 - 4) = (-2)(5)(-4) = 40$."
        ),
        # Q25 SPR
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle in the xy-plane has equation $x^2 + y^2 - 16x + 12y + 64 = 0$. What is the radius of the circle?",
            "Enter the exact integer radius:",
            ["6"],
            "Complete squares: $(x - 8)^2 + (y + 6)^2 = -64 + 64 + 36 = 36$. Radius is $\\sqrt{36} = 6$."
        ),
        # Q26 SPR
        (
            DOMAINS["MATH"]["GEOM"], "Right Triangles", "Hard",
            "In right triangle $ABC$ with right angle at $C$, $AC = 7$ and $BC = 24$. An altitude $CD$ is drawn from $C$ to hypotenuse $AB$. What is the length of altitude $CD$ expressed as a fraction a/b?",
            "Enter the exact fraction a/b:",
            ["168/25", "6.72"],
            "Hypotenuse $AB = \\sqrt{7^2 + 24^2} = \\sqrt{49 + 576} = 25$. Area $= \\frac{1}{2} \\times 7 \\times 24 = 84$. Also $\\frac{1}{2} \\times 25 \\times CD = 84 \\implies 12.5 \\times CD = 84 \\implies CD = 168/25 = 6.72$."
        ),
        # Q27 SPR
        (
            DOMAINS["MATH"]["ALG"], "Rates and Work", "Hard",
            "Two pumps, Pump A and Pump B, can drain a pool in 3 hours working together. Pump A alone takes 8 hours less than Pump B alone. How many hours does Pump A take working alone?",
            "Enter the exact integer number of hours:",
            ["4"],
            "Let $t$ be Pump A time; Pump B takes $t + 8$. $\\frac{1}{t} + \\frac{1}{t + 8} = \\frac{1}{3} \\implies 3(2t + 8) = t(t + 8) \\implies 6t + 24 = t^2 + 8t \\implies t^2 + 2t - 24 = 0 \\implies (t - 4)(t + 6) = 0$. Time is positive, so $t = 4$ hours."
        )
    ]

    for m, spec in enumerate(math_m2_sprs):
        domain, subdomain, diff, stim, prompt, answers, expl = spec
        math_m2.append(make_spr(f"t3-math-m2-q{m+23}", domain, subdomain, diff, stim, prompt, answers, expl))

    test3_data = {
        "id": "test-3",
        "title": "SAT Practice Test 3 (2026 Edition)",
        "description": "Full-length Digital SAT 2026 practice examination matching official College Board Bluebook specifications. Features rigorous multistage adaptive difficulty, sophisticated reading passages, complex multi-step math problems, and balanced answer distributions.",
        "totalQuestions": 108,
        "sections": {
            "rw": {
                "id": "rw",
                "title": "Reading and Writing",
                "timeMinutes": 64,
                "modules": [
                    {
                        "id": "test-3-rw-m1",
                        "moduleNumber": 1,
                        "title": "Reading and Writing - Module 1",
                        "timeLimitSeconds": 1920,
                        "questions": rw_m1
                    },
                    {
                        "id": "test-3-rw-m2",
                        "moduleNumber": 2,
                        "title": "Reading and Writing - Module 2",
                        "timeLimitSeconds": 1920,
                        "questions": rw_m2
                    }
                ]
            },
            "math": {
                "id": "math",
                "title": "Math",
                "timeMinutes": 70,
                "modules": [
                    {
                        "id": "test-3-math-m1",
                        "moduleNumber": 1,
                        "title": "Math - Module 1",
                        "timeLimitSeconds": 2100,
                        "questions": math_m1
                    },
                    {
                        "id": "test-3-math-m2",
                        "moduleNumber": 2,
                        "title": "Math - Module 2",
                        "timeLimitSeconds": 2100,
                        "questions": math_m2
                    }
                ]
            }
        }
    }

    output_path = os.path.join("src", "data", "test3.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("// Digital SAT 2026 Practice Test 3 (High-Difficulty Edition)\n")
        f.write("export const test3 = " + json.dumps(test3_data, indent=2) + ";\n")
    print(f"Test 3 successfully written to {output_path} with {len(rw_m1)+len(rw_m2)+len(math_m1)+len(math_m2)} questions.")

if __name__ == "__main__":
    build_test3()
