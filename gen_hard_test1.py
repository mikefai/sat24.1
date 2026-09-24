# gen_hard_test1.py
# High-Difficulty 2026 Digital SAT Practice Test 1 Generator
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

RW_TARGETS = ['B', 'A', 'D', 'C', 'A', 'B', 'C', 'D', 'C', 'A', 'D', 'B', 'D', 'B', 'A', 'C', 'A', 'D', 'B', 'C', 'C', 'B', 'D', 'A', 'B', 'C', 'A']
MATH_TARGETS = ['C', 'A', 'D', 'B', 'A', 'C', 'B', 'D', 'B', 'A', 'C', 'D', 'D', 'B', 'A', 'C', 'A', 'D', 'C', 'B', 'B', 'D']

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

def build_test1():
    rw_m1 = []
    rw_m2 = []
    math_m1 = []
    math_m2 = []

    # =========================================================================
    # TEST 1 - READING & WRITING MODULE 1 (Routing Module: Mixed Hard/Medium)
    # =========================================================================
    rw_m1_specs = [
        # Q1 Words in Context (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
            "In her historical analysis of early industrial labor unions, Dr. Aris argues that the movement's eventual success was not attributable to sudden popular enthusiasm; rather, it was the result of _____ organizing by grassroots leaders who methodically built coalitions across fractured municipal precincts over several decades.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "painstaking", ["spontaneous", "superficial", "intermittent"],
            "'Painstaking' means extremely careful, thorough, and taking great pains. The sentence contrasts 'sudden popular enthusiasm' with methodical organizing over several decades."
        ),
        # Q2 Words in Context (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Although the treaty appeared comprehensive on paper, legal scholars cautioned that its enforcement provisions were so _____ as to render any international sanctions practically unenforceable in the event of maritime border skirmishes.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "equivocal", ["stringent", "salutary", "uncompromising"],
            "'Equivocal' means ambiguous or open to multiple interpretations. If enforcement provisions are equivocal, they are too vague to allow practical enforcement."
        ),
        # Q3 Words in Context (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The archaeological discovery of bronze metallurgical kilns in the highland valley did not merely confirm local crafting traditions; it _____ the long-held archaeological consensus that highland communities had relied exclusively on lowland trade networks for metal implements.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "vitiated", ["corroborated", "dissembled", "perpetuated"],
            "'Vitiated' means impaired, invalidated, or undermined the legal or logical validity of something. The discovery contradicted and invalidated the old consensus."
        ),
        # Q4 Words in Context (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "While many contemporary commentators celebrated the CEO's charismatic proclamations as visionary breakthroughs, financial auditors warned that the company's aggressive revenue projections were largely _____ and unmoored from capital expenditure realities.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "chimerical", ["lucrative", "indispensable", "verifiable"],
            "'Chimerical' means wildly fanciful, imaginary, or unrealistic. The auditors warned that the projections were unrealistically detached from actual capital expenditures."
        ),
        # Q5 Text Structure & Purpose (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
            "Biologist Lynn Margulis initially faced widespread skepticism when she proposed endosymbiotic theory in 1967, which posited that eukaryotic organelles such as mitochondria and chloroplasts originated as free-living prokaryotic organisms engulfed by ancestral cells. For over a decade, peer reviewers dismissed her manuscripts as unsubstantiated speculation. However, subsequent sequencing of mitochondrial circular DNA and bacterial-like ribosomes definitively verified her hypothesis, fundamentally rewriting modern cellular biology.",
            "Which choice best describes the overall structure of the text?",
            "It outlines the initial scientific rejection of a novel biological hypothesis and then chronicles its eventual vindication by molecular evidence.",
            [
                "It compares two competing theories regarding cellular evolution and argues that neither provides a complete evolutionary explanation.",
                "It describes a revolutionary laboratory technique and details its failure to resolve an ongoing microbiological controversy.",
                "It praises the career of a renowned scientist while criticizing the institutional biases that delayed her initial peer recognition."
            ],
            "The passage introduces Margulis's rejected hypothesis and then explains how genetic evidence later vindicated and confirmed her theory."
        ),
        # Q6 Cross-Text Connections (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
            "<strong>Text 1</strong><br>Behavioral economists have long maintained that human decision-making is severely compromised by cognitive heuristics like hyperbolic discounting—the tendency to overvalue immediate rewards relative to future gains. In controlled laboratory experiments, subjects routinely choose small immediate payouts over significantly larger payouts delayed by only a few weeks, demonstrating fundamental human irrationality in intertemporal choice.<br><br><strong>Text 2</strong><br>Ecological anthropologists argue that labeling hyperbolic discounting 'irrational' mistakes laboratory artificiality for real-world environmental adaptation. In unpredictable or resource-volatile environments, organisms cannot guarantee that delayed rewards will ever materialize; unforeseen predators, climatic disruption, or social conflict frequently extinguish future benefits. Hence, prioritizing immediate payoffs is not a cognitive deficiency but an optimal, fitness-maximizing adaptation to existential uncertainty.",
            "Based on the texts, how would the author of Text 2 most likely respond to the claim in Text 1 regarding 'human irrationality'?",
            "By asserting that the behavior labeled irrational in laboratory settings constitutes a rational survival strategy under real-world conditions of ecological volatility.",
            [
                "By conceding that hyperbolic discounting is cognitively flawed but suggesting that educational interventions can easily rectify it.",
                "By demonstrating that laboratory participants consistently misunderstand the statistical probabilities presented by economic researchers.",
                "By arguing that hyperbolic discounting is an evolutionarily novel phenomenon that emerged only with the advent of modern financial markets."
            ],
            "Text 2 explicitly counters that prioritizing immediate rewards is a fitness-maximizing, rational adaptation to volatile real-world environments where future gains are uncertain."
        ),
        # Q7 Central Ideas & Details (Info)
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
            "Deep-sea hydrothermal vent communities exist completely detached from solar radiation, deriving ecological energy from chemosynthetic bacteria that oxidize toxic hydrogen sulfide emitting from volcanic fissures. These bacteria form dense symbiotic relationships with giant tube worms (<i>Riftia pachyptila</i>), which lack digestive tracts, mouths, and guts. Instead, the tube worms utilize specialized blood hemoglobin to transport dissolved oxygen, carbon dioxide, and hydrogen sulfide directly to an internal organ called the trophosome, where billions of symbionts convert inorganic carbon into nutrient carbohydrates for both organisms.",
            "According to the text, how do <i>Riftia pachyptila</i> tube worms obtain essential nutrition despite lacking a digestive system?",
            "They rely on internal symbiotic bacteria that convert volcanic chemical compounds into carbohydrates within a specialized organ.",
            [
                "They absorb dissolved organic molecules directly through their external chitinous protective plumes.",
                "They filter microscopic plankton and chemosynthetic microbes from surrounding hydrothermal currents.",
                "They ingest hydrothermal mineral precipitates and metabolize elemental sulfur via specialized circulatory enzymes."
            ],
            "The passage explains that symbiotic bacteria inside the trophosome organ oxidize hydrogen sulfide to synthesize nutrient carbohydrates for the tube worm."
        ),
        # Q8 Command of Evidence: Textual (Info)
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "In urban ecology, the 'habitat fragmentation hypothesis' predicts that as continuous forest tracts are segmented by suburban road networks, avian nest predation will increase sharply because predatory mammals (such as raccoons and domestic cats) exploit roadway corridors for rapid foraging access into woodland interiors. Ornithologist Dr. Kevin Vance evaluated this hypothesis by monitoring 120 artificial songbird nests containing quail eggs across forest fragments varying in perimeter-to-area ratio. If Vance's observations support the habitat fragmentation hypothesis, which finding would most strongly demonstrate this?",
            "Forest plots with high perimeter-to-area ratios that were dissected by roadways experienced significantly higher rates of nest disturbance than did expansive, undivided core forest tracts.",
            [
                "Total songbird population densities were identical in fragmented suburban woodlots and contiguous rural forest preserves.",
                "Predator mammals exhibited no measurable preference between traveling along roadway clearings and navigating dense unfragmented forest underbrush.",
                "Artificial nests situated on high canopy branches suffered equal rates of predation regardless of proximity to roads."
            ],
            "If road fragmentation facilitates predator access and increases predation, fragmented plots with high perimeter-to-area ratios and road dissections must show higher nest predation."
        ),
        # Q9 Command of Evidence: Quantitative (Info)
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Materials scientists evaluated four ceramic composite formulations (Composites W, X, Y, and Z) to determine their tensile strength retention after 1,000 thermal cycles between 200°C and 1,200°C. <br><br><table style='width:100%; border-collapse: collapse; margin: 8px 0; font-size: 13px;'><tr style='background: #f1f5f9;'><th style='border: 1px solid #cbd5e1; padding: 6px;'>Material</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Initial Tensile Strength (MPa)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Post-Cycle Strength (MPa)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Microcrack Density (cracks/mm²)</th></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Composite W</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>420</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>395</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.2</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Composite X</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>510</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>330</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>8.7</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Composite Y</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>380</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>365</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.8</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Composite Z</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>460</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>290</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>9.4</td></tr></table><br>The lead researcher concluded that formulations incorporating silicon carbide whiskers effectively inhibit thermal microfracture propagation, preserving over 90% of structural integrity.",
            "Which choice is best supported by the data in the table?",
            "Composite W retained approximately 94% of its initial tensile strength while exhibiting the lowest microcrack density among the four materials.",
            [
                "Composite X retained a higher percentage of its initial strength than did Composite Y despite experiencing severe microcracking.",
                "Composite Z exhibited the highest initial tensile strength but suffered the greatest absolute loss in structural load capacity.",
                "Every composite formulation suffered at least a 25% degradation in tensile strength following thermal cycling."
            ],
            "Composite W: 395 / 420 = 94.05% retention, and its microcrack density of 1.2 cracks/mm² is the lowest in the table."
        ),
        # Q10 Inferences (Info)
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "Paleoclimatologists analyzing speleothem calcite layers from caves in southern China noted that oxygen isotope ratios ($\delta^{18}\text{O}$) reflect historical shifts in East Asian Summer Monsoon (EASM) intensity. Lower $\delta^{18}\text{O}$ values indicate heightened precipitation and invigorated monsoon circulation. Remarkably, every major centennial-scale weakening of the EASM recorded over the past two millennia coincides precisely with agricultural collapse, nomadic migrations, and dynastic transitions documented in Chinese imperial annals. This robust chronological synchrony strongly implies that _____.",
            "abrupt climatic fluctuations exerted profound destabilizing pressures on agrarian political systems throughout premodern Chinese history",
            [
                "dynastic rulers actively suppressed historical records of catastrophic droughts to maintain administrative legitimacy",
                "cave speleothems in southern China are more reliable indicators of agricultural productivity than historical court chronicles",
                "nomadic pastoralist confederacies possessed advanced irrigation technologies that shielded them from monsoon failures"
            ],
            "The direct correlation between monsoon weakenings (droughts/reduced rain) and dynastic falls/agricultural collapse indicates that climatic disruption heavily destabilized agrarian dynasties."
        ),
        # Q11 Standard English Conventions: Boundaries
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "During the Italian Renaissance, master fresco painters had to apply ground mineral pigments directly onto wet lime _____ chemical carbonation would lock the colors into the structural plaster permanently.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "plaster; as the drying plaster absorbed atmospheric carbon dioxide,",
            [
                "plaster, as the drying plaster absorbed atmospheric carbon dioxide,",
                "plaster, which as the drying plaster absorbed atmospheric carbon dioxide",
                "plaster as the drying plaster absorbed atmospheric carbon dioxide"
            ],
            "A semicolon is required to separate the two independent clauses: 'master fresco painters had to apply...' and 'chemical carbonation would lock...' (which has the dependent clause 'as the drying plaster...'). A comma alone produces a comma splice."
        ),
        # Q12 Standard English Conventions: Modifiers
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Synthesizing archival records with advanced isotopic bone _____ bioarchaeologist Dr. Miriam Chen demonstrated that the nomadic pastoralists engaged in extensive millet cultivation centuries earlier than previously hypothesized.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "chemistry,",
            [
                "chemistry and",
                "chemistry",
                "chemistry; while"
            ],
            "The introductory participial phrase ('Synthesizing archival records with advanced isotopic bone chemistry,') must be followed immediately by a comma and the logical subject who performed the action ('bioarchaeologist Dr. Miriam Chen')."
        ),
        # Q13 Standard English Conventions: Subject-Verb Agreement
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Neither the extensive computational models developed by the climatology consortium nor the empirical telemetry recorded from deep oceanic sensor _____ sufficient to explain the sudden deceleration of the North Atlantic subpolar gyre.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "buoys was",
            [
                "buoys were",
                "buoys, being",
                "buoys having been"
            ],
            "In a 'neither... nor...' construction with subjects of different number, the verb agrees with the subject closest to it. Wait: 'telemetry' is an uncountable singular noun! 'sensor buoys' is in the prepositional phrase 'from deep oceanic sensor buoys', so the subject is 'telemetry', which is singular, requiring 'was'."
        ),
        # Q14 Standard English Conventions: Punctuation (Nonrestrictive)
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "Astronomer Vera Rubin gathered empirical rotational curves of spiral galaxies that contradicted Newtonian _____ stars at the galactic periphery orbited with velocities identical to stars situated near the bright galactic core.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "expectations: unexpectedly,",
            [
                "expectations, unexpectedly",
                "expectations; unexpectedly",
                "expectations unexpectedly"
            ],
            "A colon is used to introduce an explanation, elaboration, or surprising specification of what the contradictory expectations revealed."
        ),
        # Q15 Transitions (Expression)
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
            "Early solar photovoltaic cells constructed from crystalline silicon exhibited an energy conversion efficiency of barely 6% in 1954. _____, modern multi-junction perovskite-silicon tandem cells routinely surpass 33% efficiency in laboratory benchmarks, approaching the thermodynamic limits of single-junction architectures.",
            "Which choice completes the text with the most logical transition?",
            "Today",
            ["Consequently", "For instance", "In other words"],
            "The passage contrasts historical early efficiency in 1954 with current modern efficiency, making 'Today' the correct chronological contrast transition."
        ),
        # Q16 Transitions (Expression)
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Critics argued that the construction of municipal sea walls would disrupt fragile shoreline sediment transport and destroy intertidal mudflats. _____, coastal engineers demonstrated that integrating permeable riprap revetments with artificial oyster reefs would dissipate wave kinetic energy while actively promoting wetland accretion.",
            "Which choice completes the text with the most logical transition?",
            "Conversely",
            ["Furthermore", "For example", "Therefore"],
            "The passage contrasts the critics' negative predictions with the coastal engineers' opposing positive findings, requiring the contrast transition 'Conversely'."
        ),
        # Q17 Rhetorical Synthesis (Expression)
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The James Webb Space Telescope (JWST) operates at an orbit around the Sun-Earth Lagrange point 2 (L2).</li><li style='margin-bottom: 4px;'>L2 is located approximately 1.5 million kilometers from Earth.</li><li style='margin-bottom: 4px;'>JWST observes predominantly in the infrared spectrum.</li><li style='margin-bottom: 4px;'>Its primary beryllium mirror measures 6.5 meters in diameter.</li><li style='margin-bottom: 4px;'>Because of its infrared capability and massive mirror, JWST can observe high-redshift galaxies formed less than 400 million years after the Big Bang.</li></ul>",
            "The student wants to emphasize how JWST's optical specifications enable the study of early cosmic history. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "Equipped with a 6.5-meter mirror and infrared detection capabilities, the James Webb Space Telescope can observe ancient high-redshift galaxies that formed within 400 million years of the Big Bang.",
            [
                "Orbiting at Lagrange point 2 roughly 1.5 million kilometers from Earth, the James Webb Space Telescope features a primary mirror constructed from beryllium.",
                "The James Webb Space Telescope observes the universe primarily across infrared wavelengths from an orbital location known as L2.",
                "Measuring 6.5 meters across, the primary mirror of the James Webb Space Telescope is significantly larger than previous orbital telescopes."
            ],
            "The correct choice directly connects the optical specifications (6.5-meter mirror, infrared detection) to the goal (studying ancient galaxies formed shortly after the Big Bang)."
        ),
        # Q18 Words in Context (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The historian emphasized that medieval court chronicles were rarely objective depositions; rather, scribes frequently framed political assassinations in _____ terms, depicting the dynastic usurpations as divine retributions for moral failings.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "didactic", ["utilitarian", "tangential", "clandestine"],
            "'Didactic' means intended to instruct, particularly in moral lessons. Depicting political usurpations as divine moral retributions represents a didactic framing."
        ),
        # Q19 Text Structure & Purpose (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In his 1903 treatise on sociology, W.E.B. Du Bois introduced the concept of 'double consciousness,' describing the internal psychological conflict experienced by African Americans living in an oppressive society: 'this sense of always looking at one's self through the eyes of others, of measuring one's soul by the tape of a world that looks on in amused contempt and pity.' Du Bois does not merely describe this psychological state as an affliction; he identifies it as a source of distinctive epistemological insight, endowing African Americans with a 'second-sight' capable of perceiving the deep contradictions beneath American democratic ideals.",
            "Which choice best describes the main function of the underlined portion ('he identifies it as a source of distinctive epistemological insight...')?",
            "It shifts the focus from a purely psychological pathology to a profound analytical capability that enables critical perception of societal contradictions.",
            [
                "It dismisses Du Bois's initial definition of double consciousness as an outdated artifact of early twentieth-century racial sociology.",
                "It provides statistical evidence corroborating the prevalence of psychological distress among minority populations in democratic nations.",
                "It contrasts Du Bois's sociological theories with the economic frameworks advanced by his contemporary Booker T. Washington."
            ],
            "The passage contrasts viewing double consciousness simply as an affliction with Du Bois's view that it provides unique insight ('second-sight') into democratic contradictions."
        ),
        # Q20 Central Ideas & Details (Info)
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "Prion diseases, such as Creutzfeldt-Jakob disease, represent an unprecedented biological paradigm because the infectious agent is completely devoid of genetic nucleic acids (DNA or RNA). The disease propagates when an abnormally folded isoform of the cellular prion protein ($\text{PrP}^\text{Sc}$) encounters normal cellular prion proteins ($\text{PrP}^\text{C}$), inducing them to refold into the infectious $\beta$-sheet-rich conformation through template-directed misfolding. These misfolded proteins aggregate into insoluble amyloid fibrils that induce neurodegenerative spongiform vacuolation in cerebral cortex tissue, impervious to conventional autoclaving and enzymatic proteolysis.",
            "Which statement regarding prion propagation is most directly supported by the text?",
            "Prions multiply by mechanically altering the three-dimensional structural conformation of native cellular proteins rather than replicating genetic material.",
            [
                "Prion replication requires host cellular viral reverse transcriptase to synthesize abnormal neurodegenerative polypeptides.",
                "Standard laboratory sterilization methods like autoclaving reliably neutralize prion infectiousness by hydrolyzing peptide backbones.",
                "The primary catalyst for prion aggregation is a chemical mutation that converts host DNA into misfolded ribonucleic acids."
            ],
            "The passage explicitly states prions lack nucleic acids and propagate when misfolded prions induce normal proteins to refold into the infectious conformation."
        ),
        # Q21 Command of Evidence (Info)
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Plant evolutionary biologist Dr. Hiroshi Tanaka investigated whether the evolution of CAM (crassulacean acid metabolism) photosynthesis in desert succulents constitutes an adaptation strictly for water preservation or whether it also confers significant thermal tolerance. Tanaka measured stomatal conductance and internal leaf temperature in <i>Agave tequilana</i> specimens under high drought conditions ($38^\circ\text{C}$, $15\%$ soil moisture) compared to control conditions ($24^\circ\text{C}$, $65\%$ moisture). If Tanaka's findings support the water preservation hypothesis over the thermal tolerance hypothesis, which result would most directly support this?",
            "Stomatal closure during scorching daylight hours reduced transpiration water loss by 82% without producing any measurable reduction in internal midday leaf tissue temperatures.",
            [
                "Internal leaf temperatures dropped significantly during daylight hours despite persistent stomatal aperture closure.",
                "Specimens subjected to drought exhibited higher photosynthetic carbon assimilation rates at noon than did irrigated control specimens.",
                "High nighttime humidity caused plants to abandon nighttime malate storage in favor of standard C3 photosynthetic pathways."
            ],
            "If CAM photosynthesis is strictly for water conservation and not thermal cooling, stomata closing during the day will prevent water loss without reducing leaf temperature."
        ),
        # Q22 Inferences (Info)
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In high-energy physics, the observation of neutrino oscillations demonstrated that neutrinos possess non-zero rest masses, defying the minimal Standard Model where neutrinos are strictly massless. Because neutrino masses are astonishingly tiny—less than one-millionth the mass of an electron—theorists proposed the 'seesaw mechanism,' which posits that the known light neutrinos obtain their minuscule masses through quantum mixing with undiscovered, ultra-heavy Majorana neutrinos. If experimental searches at the Large Hadron Collider definitively rule out the existence of such heavy Majorana partners up to the Planck energy scale, physicists would be forced to conclude that _____.",
            "the origin of neutrino mass requires an alternative theoretical mechanism beyond the canonical high-energy seesaw framework",
            [
                "neutrinos must actually be completely massless particles conforming exactly to the minimal Standard Model",
                "neutrino oscillation phenomena observed in subterranean detectors were the result of systematic measurement errors",
                "neutrinos cannot interact with the Higgs boson or any other fundamental scalar fields in quantum field theory"
            ],
            "Ruling out the heavy Majorana neutrinos eliminates the seesaw mechanism, forcing physicists to look for an alternative mechanism to explain observed non-zero mass."
        ),
        # Q23 Standard English Conventions (Boundaries)
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "In 1912, Alfred Wegener published his continental drift hypothesis, marshal-ling geological similarities across transatlantic coastlines _____ most geophysicists vehemently rejected his ideas because he could not propose a plausible geophysical propulsion mechanism.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "nevertheless, at that time,",
            [
                "nevertheless at that time",
                "; nevertheless, at that time,",
                ", nevertheless at that time"
            ],
            "Wait: 'In 1912, Alfred Wegener published his continental drift hypothesis, marshalling geological similarities across transatlantic coastlines' is an independent clause. 'most geophysicists vehemently rejected his ideas...' is a second independent clause. A semicolon followed by 'nevertheless, at that time,' is the grammatically correct boundary!"
        ),
        # Q24 Standard English Conventions (Form/Structure)
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Exceeding the carrying capacity of their fragile subalpine tundra _____ populations of feral mountain goats in Olympic National Park degraded delicate endemic wildflower meadows, prompting federal wildlife managers to initiate helicopter relocations.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "habitat,",
            [
                "habitat; the",
                "habitat, and the",
                "habitat the"
            ],
            "The introductory participial phrase ('Exceeding the carrying capacity of their fragile subalpine tundra habitat,') must be followed by a comma, and the subject being modified is 'populations of feral mountain goats'."
        ),
        # Q25 Transitions (Expression)
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Proponents of nuclear fusion energy highlight its near-limitless deuterium fuel supply and zero greenhouse gas emissions. _____, monumental engineering hurdles—including stabilizing plasma turbulence at 100 million Kelvin and mitigating neutron damage to reactor walls—continue to delay commercial grid deployment.",
            "Which choice completes the text with the most logical transition?",
            "That said,",
            ["In addition,", "Specifically,", "Consequently,"],
            "'That said' introduces a major qualifying contrast or concession against the initial enthusiastic claims of fusion energy."
        ),
        # Q26 Rhetorical Synthesis (Expression)
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The Antikythera mechanism is an ancient Greek analog computer retrieved from an Aegean shipwreck in 1901.</li><li style='margin-bottom: 4px;'>Dating to circa 150–100 BCE, it contains over 30 precision bronze gears.</li><li style='margin-bottom: 4px;'>It calculated and displayed astronomical cycles, solar eclipses, and lunar phases.</li><li style='margin-bottom: 4px;'>It accurately accounted for the Moon's variable orbital speed using an innovative pin-and-slot epicyclic gear arrangement.</li><li style='margin-bottom: 4px;'>Mechanical complexity of this level was not seen again in Europe until medieval clockwork mechanisms 1,400 years later.</li></ul>",
            "The student wants to emphasize the unprecedented mechanical sophistication of the Antikythera mechanism. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "Featuring an innovative pin-and-slot gear system to model the Moon's irregular orbital velocity, the Antikythera mechanism achieved a level of astronomical computation and mechanical complexity not matched until European clockwork 1,400 years later.",
            [
                "Recovered from an Aegean shipwreck in 1901, the bronze Antikythera mechanism dates to approximately 150–100 BCE.",
                "The Antikythera mechanism utilized more than 30 bronze gears to predict solar eclipses and tracking lunar cycles in ancient Greece.",
                "European artisans developed complex astronomical clockwork during the medieval era, over a millennium after ancient Greek gears were cast."
            ],
            "The choice directly fulfills the goal of highlighting unprecedented mechanical sophistication (modeling irregular orbital velocity with pin-and-slot gears; complexity unmatched for 1,400 years)."
        ),
        # Q27 Words in Context (Craft)
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Far from being an immutable canon carved in stone, the legal scholar argued that constitutional law is an inherently _____ framework, continually reinterpreted and reshaped by successive judicial generations to address unprecedented economic and technological exigencies.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "malleable", ["indolent", "dogmatic", "archaic"],
            "'Malleable' means adaptable or capable of being reshaped. It directly contrasts with 'immutable canon carved in stone' and aligns with 'continually reinterpreted and reshaped'."
        )
    ]

    for i, spec in enumerate(rw_m1_specs):
        target_letter = RW_TARGETS[i]
        if len(spec) == 7:
            domain, subdomain, diff, stim, corr, dists, expl = spec
            prompt = "Which choice most logically completes the text?" if "_____" in stim else "Which finding, if true, most strongly supports the hypothesis?"
        else:
            domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        # Handle boundary question 23 semicolon
        if i == 22:
            corr = "; nevertheless, at that time,"
            dists = [", nevertheless at that time", "nevertheless at that time,", "nevertheless, at that time"]
        rw_m1.append(make_hard_mcq(f"t1-rw-m1-q{i+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # =========================================================================
    # TEST 1 - READING & WRITING MODULE 2 (Adaptive Hard Module: 100% Hard/Upper-Med)
    # =========================================================================
    rw_m2_specs = [
        # Q1 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The diplomat recognized that issuing a public ultimatum would merely entrench the adversarial government's defensive posturing; instead, she engaged in _____ backchannel discussions to negotiate bilateral disarmament concessions without inciting domestic nationalist uproar.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "discreet", ["ostentatious", "insolent", "precipitous"],
            "'Discreet' means circumspect, unobtrusive, or careful to avoid public embarrassment. The contrast with a public ultimatum confirms 'discreet backchannel discussions'."
        ),
        # Q2 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Despite the author's extensive citations of primary colonial diaries, literary historians criticized the novel for its _____ depiction of seventeenth-century domestic life, arguing that the characters' egalitarian sensibilities were anachronistic projections of modern secular values.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "spurious", ["unimpeachable", "austere", "pellucid"],
            "'Spurious' means illegitimate, false, or not genuine. The historians criticized the depiction as anachronistic projections of modern values rather than genuine history."
        ),
        # Q3 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "Rather than viewing political polarization as an entirely modern malady, historical political theorists argue that factional dispute is an _____ facet of popular democracy, naturally arising whenever citizens possess the liberty to express conflicting material interests.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "inexorable", ["ephemeral", "anomalous", "esoteric"],
            "'Inexorable' means impossible to prevent or stop; inevitable. The theorists argue factional dispute is inevitable whenever freedom exists."
        ),
        # Q4 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The bioethicist argued that gene drives capable of eradicating disease-carrying mosquito species should not be released into wild ecosystems without international consensus; the potential for irreversible ecological disruption is simply too _____ to justify unilateral national experimentation.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "momentous", ["trifling", "nebulous", "quixotic"],
            "'Momentous' means of immense consequence or importance. The risk of irreversible ecological disruption is of immense significance."
        ),
        # Q5 Text Structure & Purpose
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In <i>The Structural Transformation of the Public Sphere</i> (1962), German philosopher Jürgen Habermas historicized the emergence of a bourgeois public sphere in eighteenth-century European coffeehouses and salons, where private individuals assembled to debate civic governance through rational-critical discourse uninhibited by feudal hierarchies. Habermas acknowledges that this early public sphere was idealistically egalitarian in theory yet exclusionary in practice, systematically barring women, the working class, and colonial subjects. Nevertheless, he argues that the foundational ideal of rational communicative action established an enduring normative benchmark by which modern democratic institutions can critically evaluate their own democratic deficits.",
            "Which choice best describes the function of the underlined portion ('Nevertheless, he argues that the foundational ideal...') in the passage as a whole?",
            "It asserts that despite its historical exclusionary shortcomings, the conceptual ideal of the public sphere provides a valuable normative standard for critiquing contemporary governance.",
            [
                "It proves that eighteenth-century bourgeois salons were genuinely more democratic than contemporary parliamentary democracies.",
                "It repudiates the critiques of modern feminist historians by asserting that class exclusions were necessary for rational discourse.",
                "It traces how modern digital communications platforms have perfectly restored the deliberative democracy of Enlightenment salons."
            ],
            "The passage concedes exclusionary practices but emphasizes that the underlying ideal remains an enduring normative standard to evaluate modern democracy."
        ),
        # Q6 Cross-Text Connections
        (
            DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
            "<strong>Text 1</strong><br>Psycholinguist Noam Chomsky's Universal Grammar framework posits that humans are born with an innate, genetically encoded language acquisition device (LAD). According to this view, the superficial syntactic diversity of the world's 7,000 languages conceals a deep, universal computational blueprint comprising discrete principles (such as recursion and hierarchical structure). Proponents point to the 'poverty of the stimulus'—the fact that children rapidly master complex grammatical rules from messy and incomplete speech inputs without explicit instruction—as definitive proof of innate grammatical knowledge.<br><br><strong>Text 2</strong><br>Cognitive linguist Michael Tomasello and usage-based theorists reject the necessity of an innate Universal Grammar. Instead, they demonstrate through longitudinal child development corpora that language acquisition is achieved through general-purpose human cognitive mechanisms: statistical pattern-recognition and intention-reading. Children do not access abstract pre-programmed universal trees; rather, they gradually build linguistic competence by generalizing from specific lexical tokens and communicative interactions encountered in daily social scaffolding.",
            "Based on the texts, how would the author of Text 2 most likely respond to the 'poverty of the stimulus' argument cited in Text 1?",
            "By contending that powerful general-purpose statistical pattern-recognition and social scaffolding provide children with sufficient information to master grammar without innate rules.",
            [
                "By demonstrating that children only master grammatical language after receiving formal classroom linguistic instruction in elementary school.",
                "By asserting that the 7,000 languages of the world share identical surface syntaxes that make learning effortless.",
                "By arguing that recursion is biologically impossible in human speech processing due to working memory constraints."
            ],
            "Text 2 counters that general-purpose cognitive mechanisms (statistical pattern-recognition and social intention-reading) explain language acquisition without requiring an innate Universal Grammar."
        ),
        # Q7 Central Ideas & Details
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "Ecosystem resilience in tropical coral reefs depends critically on functional redundancy among herbivorous reef fish. Parrotfish (family Scaridae) and surgeonfish (family Acanthuridae) graze on fleshy macroalgae that compete with reef-building stony corals (<i>Scleractinia</i>) for substrate and sunlight. When overfishing removes large scarid parrotfish, surgeonfish can partially compensate by cropping turf algae; however, surgeonfish possess finer pharyngeal jaws incapable of bioeroding calcified carbonate or scraping deep crustose coralline algae. Consequently, without parrotfish, macroalgae swiftly smother juvenile coral polyps, triggering a catastrophic phase shift from coral-dominated reefs to degraded algal wastelands.",
            "Which choice most accurately characterizes the ecological limitation of surgeonfish described in the passage?",
            "Although surgeonfish consume turf algae, their jaw morphology prevents them from scraping calcified substrate or clearing deep macroalgae as parrotfish do.",
            [
                "Surgeonfish actively consume juvenile stony coral polyps when macroalgae populations become depleted by parrotfish.",
                "Surgeonfish are rapidly extirpated by predatory reef sharks when coral canopy complexity declines.",
                "Surgeonfish grazing accelerates the catastrophic phase shift toward algal dominance by fertilizing macroalgal blooms."
            ],
            "The text states surgeonfish have finer jaws that cannot bioerode calcified carbonate or scrape deep algae, meaning they cannot fully substitute for parrotfish."
        ),
        # Q8 Command of Evidence: Textual
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Neuroscientist Dr. Leona Vance investigated the 'synaptic homeostasis hypothesis,' which proposes that the biological function of slow-wave sleep is to scale down the total synaptic strength accumulated across the brain during wakefulness, thereby preventing metabolic overload and restoring cognitive baseline capacity. Vance recorded miniature excitatory postsynaptic currents (mEPSCs) in pyramidal neurons of rodents across 12 hours of sustained wakefulness versus 8 hours of uninterrupted slow-wave sleep. If Vance's empirical data validate the synaptic homeostasis hypothesis, which finding would be observed?",
            "Average mEPSC amplitudes and synaptic spine densities were significantly elevated after sustained wakefulness and systematically renormalized downward following slow-wave sleep.",
            [
                "Synaptic spine densities remained completely constant across both wake and sleep cycles while axonal firing rates doubled during slow-wave sleep.",
                "Rodents deprived of sleep exhibited a precipitous decline in total cerebral glucose consumption and widespread synaptic atrophy.",
                "Slow-wave sleep triggered a selective amplification of high-frequency synaptic connections in the sensory cortex while scaling down the hippocampus."
            ],
            "If the hypothesis is correct, wakefulness builds up synaptic strength (elevated mEPSCs/spine density) and slow-wave sleep scales it down (renormalization)."
        ),
        # Q9 Command of Evidence: Quantitative
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Agronomists evaluated four drought-tolerant maize cultivars (Lines Alpha, Beta, Gamma, and Delta) grown under induced moisture deficit (25% field capacity) to measure grain yield and water-use efficiency (WUE, kg grain per m³ water).<br><br><table style='width:100%; border-collapse: collapse; margin: 8px 0; font-size: 13px;'><tr style='background: #f1f5f9;'><th style='border: 1px solid #cbd5e1; padding: 6px;'>Maize Cultivar</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Yield under Irrigation (t/ha)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Yield under Drought (t/ha)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>WUE under Drought (kg/m³)</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Yield Reduction (%)</th></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Line Alpha</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>9.8</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>5.2</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.45</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>46.9%</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Line Beta</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>8.4</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>6.1</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.92</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>27.4%</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Line Gamma</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>10.2</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>4.8</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.28</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>52.9%</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Line Delta</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>7.9</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>5.8</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>1.81</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>26.6%</td></tr></table><br>The researchers concluded that Line Beta represents the superior candidate for commercial drought-prone deployment because it couples the highest absolute yield under drought with superior water-use efficiency.",
            "Which statement is best supported by the data in the table?",
            "Line Beta achieved the highest drought yield (6.1 t/ha) and the highest water-use efficiency (1.92 kg/m³) while experiencing a lower percentage yield reduction than Line Alpha or Line Gamma.",
            [
                "Line Gamma was the most resilient cultivar because it produced the highest yield under fully irrigated conditions.",
                "Line Delta suffered a greater percentage yield reduction than any other cultivar evaluated in the trial.",
                "Line Alpha consumed less water per kilogram of grain produced under drought stress than did Line Beta."
            ],
            "The table shows Line Beta has highest drought yield (6.1), highest WUE (1.92), and only 27.4% reduction (much lower than Alpha's 46.9% and Gamma's 52.9%)."
        ),
        # Q10 Inferences
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In economic history, the 'resource curse' or 'Dutch disease' describes an apparent paradox: nations endowed with abundant natural resource reserves (such as petroleum or minerals) frequently experience slower long-term economic growth, lower industrial diversification, and higher currency volatility than nations lacking natural wealth. When natural resource export revenues surge, the domestic currency appreciates sharply on international foreign exchange markets, making domestic manufacturing and agricultural exports uncompetitively expensive abroad. Over time, manufacturing capital and skilled labor migrate into the extractive resource sector, leaving the broader economy hollowed out. It can reasonably be inferred from the passage that a government seeking to mitigate Dutch disease during a resource boom should _____.",
            "divert resource revenues into sovereign wealth funds invested in foreign assets to suppress artificial currency appreciation and preserve industrial export competitiveness",
            [
                "subsidize domestic mining conglomerates to maximize extraction volumes before global commodity prices crash",
                "impose severe import tariffs on foreign manufactured goods to forcibly eliminate domestic reliance on international trade",
                "mandate that manufacturing firms relocate their headquarters to extractive resource extraction zones"
            ],
            "To prevent currency appreciation that harms domestic manufacturing, governments invest resource revenues abroad in sovereign wealth funds, keeping exchange rates stable."
        ),
        # Q11 Standard English Conventions: Boundaries
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "By deploying radio telemetry to track leatherback sea turtles across the Pacific, marine ecologist Dr. Helen Thorne discovered that post-nesting females undertake thousands of kilometers of trans-oceanic _____ ocean currents alone cannot account for their precise navigation toward temperate foraging grounds.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "migration; passive",
            [
                "migration, passive",
                "migration passive",
                "migration, and passive"
            ],
            "Two complete independent clauses: 'marine ecologist Dr. Helen Thorne discovered that post-nesting females undertake thousands of kilometers of trans-oceanic migration' and 'passive ocean currents alone cannot account...' Semicolon correctly links them."
        ),
        # Q12 Standard English Conventions: Modifiers
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Having decoded the intricate cuneiform administrative tablets excavated at ancient _____ the economic historian demonstrated that Mesopotamian temple complexes functioned as sophisticated centralized banking systems with formal credit accounting.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "Uruk,",
            [
                "Uruk;",
                "Uruk, and",
                "Uruk where"
            ],
            "The introductory participial phrase ('Having decoded the intricate cuneiform administrative tablets excavated at ancient Uruk,') must be followed by a comma, and the subject is 'the economic historian'."
        ),
        # Q13 Standard English Conventions: Subject-Verb Agreement
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "The discovery of fossilized melanosomes in exceptionally preserved feathered dinosaur specimens from Liaoning _____ that structural coloration and iridescent plumage evolved tens of millions of years prior to the radiation of crown birds.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "demonstrates",
            [
                "demonstrate",
                "demonstrating",
                "have demonstrated"
            ],
            "The subject of the sentence is the singular noun 'The discovery' (not 'melanosomes' or 'specimens', which are objects of prepositions), requiring the singular verb 'demonstrates'."
        ),
        # Q14 Standard English Conventions: Punctuation (Dashes)
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "The fundamental pillars of the Standard Model of particle physics—quarks, leptons, and gauge _____ have withstood five decades of intense experimental bombardment at CERN without revealing a single unpredicted flaw.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "bosons—",
            [
                "bosons,",
                "bosons;",
                "bosons"
            ],
            "An em-dash is opened before 'quarks' ('particle physics—quarks, leptons, and gauge bosons—'), so an em-dash must close the parenthetical appositive."
        ),
        # Q15 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Classical macroeconomists argued that government interventions during market downturns inevitably cause distortionary inflation and impede private capital reallocation. _____, Keynesian theorists maintained that during severe liquidity traps, private aggregate demand collapses so profoundly that only counter-cyclical deficit spending can restore employment equilibria.",
            "Which choice completes the text with the most logical transition?",
            "By contrast,",
            ["Accordingly,", "In fact,", "Similarly,"],
            "The passage contrasts the classical viewpoint (hands-off government) with the Keynesian viewpoint (counter-cyclical intervention), making 'By contrast' the precise transition."
        ),
        # Q16 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Urban developers initially assumed that constructing elevated highway bypasses would relieve chronic traffic gridlock in the city center. _____, traffic congestion worsened significantly over the subsequent five years as reduced travel times stimulated latent commuter demand, a phenomenon urban planners term 'induced travel demand.'",
            "Which choice completes the text with the most logical transition?",
            "Instead,",
            ["Likewise,", "For example,", "Hence,"],
            "The sentence demonstrates that the opposite of the developers' assumption occurred; rather than gridlock being relieved, congestion worsened. 'Instead' conveys this counter-result."
        ),
        # Q17 Rhetorical Synthesis
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>Bioluminescence in marine organisms is generated by the oxidation of a luciferin substrate catalyzed by a luciferase enzyme.</li><li style='margin-bottom: 4px;'>Dinoflagellates emit flashes of blue-green light (~470 nm) in response to mechanical shear stress caused by waves or predators.</li><li style='margin-bottom: 4px;'>This flash acts as a 'burglar alarm,' illuminating grazing copepods and attracting secondary predators to consume the grazers.</li><li style='margin-bottom: 4px;'>Blue-green light travels further through oceanic water columns than any other visible wavelength.</li><li style='margin-bottom: 4px;'>Over 75% of deep-sea pelagic organisms possess bioluminescent capabilities.</li></ul>",
            "The student wants to explain the ecological defense mechanism of dinoflagellate bioluminescence. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "When disturbed by mechanical shear stress from grazers, dinoflagellates emit blue-green bioluminescent flashes that act as a 'burglar alarm,' illuminating predators to attract secondary carnivores.",
            [
                "Bioluminescence is a chemical reaction occurring in over 75% of deep-sea organisms when luciferin is oxidized by luciferase.",
                "Because blue-green light at 470 nanometers penetrates further through water columns than red light, many marine creatures emit flashes.",
                "Dinoflagellates are microscopic marine plankton that produce blue-green light whenever ocean currents create mechanical shear stress."
            ],
            "The correct choice directly explains the ecological defense mechanism: emitting flashes as a 'burglar alarm' that exposes predators to secondary carnivores."
        ),
        # Q18 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "While the political orator's speeches were filled with passionate appeals and florid metaphors, policy analysts dismissed his platform as completely _____, pointing out that none of his proposed statutory reforms contained actionable fiscal appropriations.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "vacuous", ["trenchant", "unprecedented", "imperious"],
            "'Vacuous' means devoid of substance, empty, or meaningless. The analysts dismissed the platform because it lacked actionable substance or fiscal appropriations."
        ),
        # Q19 Text Structure & Purpose
        (
            DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
            "In historical climatology, the 'Little Ice Age' (spanning approximately 1300 to 1850 CE) was characterized by widespread cooling across the Northern Hemisphere. Historically, scholars attributed this multi-century cooling episode to reduced solar irradiance (such as the Maunder Minimum) and frequent explosive volcanic eruptions injecting sulfate aerosols into the stratosphere. However, recent high-resolution ice-core analyses by Dr. Matthew Toohey suggest an intriguing compounding anthropogenic factor: the massive reforestation of indigenous agricultural lands across the Americas following European epidemic contact sequestered billions of tons of atmospheric carbon dioxide, thereby reinforcing global radiative cooling.",
            "Which choice best describes the relationship between the two sentences?",
            "The first sentence presents the prevailing conventional explanation for a historical climatic phenomenon, and the second sentence introduces a complementary anthropogenic mechanism supported by recent ice-core evidence.",
            [
                "The first sentence defines an unresolved meteorological dispute, and the second sentence provides experimental data that definitively invalidates solar theories.",
                "The first sentence describes a severe ecological catastrophe, and the second sentence details the technological interventions medieval societies used to reverse it.",
                "The first sentence chronicles agricultural practices in pre-Columbian America, and the second sentence explains their relationship to volcanic sulfate eruptions."
            ],
            "Sentence 1 outlines the conventional causes (volcanoes, solar minimum); sentence 2 introduces the complementary reforestation CO2 sequestration mechanism."
        ),
        # Q20 Central Ideas & Details
        (
            DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Hard",
            "The blood-brain barrier (BBB) is a highly selective semipermeable border of brain capillary endothelial cells connected by complex tight junctions (claudins, occludins, and junctional adhesion molecules). While the BBB effectively shields neural parenchyma from circulating systemic pathogens, neurotoxins, and inflammatory cytokines, its exceptional selectivity presents a formidable obstacle for pharmacotherapy, blocking more than 98% of small-molecule neurotherapeutics and virtually all macromolecular biopharmaceuticals (including monoclonal antibodies and viral gene vectors) from accessing the central nervous system.",
            "Which choice best summarizes the clinical dilemma highlighted in the passage?",
            "The anatomical mechanism that shields the brain from systemic toxins simultaneously prevents the overwhelming majority of therapeutic drugs from reaching diseased neural tissue.",
            [
                "Tight junctions in brain capillary endothelial cells degrade rapidly when exposed to therapeutic monoclonal antibodies.",
                "Neurodegenerative pathogens exploit claudin proteins to breach the blood-brain barrier and infect the central nervous system.",
                "Small-molecule pharmaceuticals are more toxic to cerebral microvessels than macromolecular viral gene vectors."
            ],
            "The clinical dilemma is that the protective selectivity of the BBB also keeps out over 98% of therapeutic molecules."
        ),
        # Q21 Command of Evidence
        (
            DOMAINS["RW"]["INFO"], "Command of Evidence", "Hard",
            "Evolutionary biologists debated whether the elaborate plumage of male birds-of-paradise evolved through the 'good genes' hypothesis (plumage ornaments honestly signal genetic resistance to debilitating parasites) or the 'runaway sexual selection' hypothesis (plumage evolves through arbitrary female aesthetic preferences uncoupled from survival fitness). Dr. Clara Ruiz evaluated 200 male <i>Paradisaea raggiana</i> individuals, scoring tail ornament length, blood parasite load (<i>Haemoproteus</i> titers), and annual offspring survival rates. Which finding, if true, would most strongly support the 'good genes' hypothesis over the 'runaway sexual selection' hypothesis?",
            "Males with the longest and most symmetrical ornamental plumes exhibited significantly lower blood parasite titers, and their offspring survived to reproductive maturity at a rate 40% higher than the offspring of less ornamented males.",
            [
                "Females exhibited strong mating preferences for males with longer plumes regardless of whether those males were infected with blood parasites.",
                "Male tail ornament length correlated with higher mortality from predatory raptors during seasonal courtship displays.",
                "Offspring of highly ornamented males inherited identical plume dimensions but demonstrated no measurable difference in immune resistance compared to the general population."
            ],
            "Good genes requires honest signaling: more ornamented males have fewer parasites and sire offspring with higher survival fitness."
        ),
        # Q22 Inferences
        (
            DOMAINS["RW"]["INFO"], "Inferences", "Hard",
            "In cognitive neuroscience, the 'predictive processing' framework asserts that the human brain does not passively process incoming sensory streams. Instead, it functions as a Bayesian inference machine that continuously generates top-down predictions about the causes of sensory inputs, updating its internal generative model only when a 'prediction error'—a mismatch between expectation and incoming sensory data—is registered. When sensory input matches predictions perfectly, sensory signals are effectively silenced or attenuated at lower cortical levels. It follows from this framework that sensory signals ascending from peripheral receptors to higher cortical processing centers primarily represent _____.",
            "the discrepancies between prior top-down internal hypotheses and actual bottom-up sensory feedback",
            [
                "complete, unfiltered reproductions of the physical environment captured by sensory organs",
                "random neural noise that higher associative brain regions must actively suppress through motor inhibition",
                "evolutionarily static cognitive templates that remain impervious to experiential modification"
            ],
            "Under predictive processing, signals that ascend are 'prediction errors'—the discrepancies between top-down hypotheses and bottom-up sensory data."
        ),
        # Q23 Standard English Conventions (Boundaries)
        (
            DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
            "In 1938, physicists Lise Meitner and Otto Frisch calculated that the nuclear fission of uranium releases approximately 200 million electron volts of kinetic energy per _____ immense quantity that Frisch famously described as verifying Einstein's mass-energy equivalence equation.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "atom, an",
            [
                "atom an",
                "atom; an",
                "atom: being an"
            ],
            "'an immense quantity that Frisch famously described...' is an appositive phrase modifying the 200 million electron volts. A comma ('atom, an') is the correct punctuation."
        ),
        # Q24 Standard English Conventions (Form/Structure)
        (
            DOMAINS["RW"]["CONV"], "Form, Structure, and Sense", "Hard",
            "Neither the sudden increase in global agricultural fertilizer consumption nor the expansion of municipal wastewater treatment _____ sufficient to explain the localized surge of toxic cyanobacteria blooms in Lake Erie.",
            "Which choice completes the text so that it conforms to the conventions of Standard English?",
            "facilities was",
            [
                "facilities were",
                "facilities, being",
                "facilities having been"
            ],
            "Wait: 'Neither the sudden increase... nor the expansion...' Both subjects are singular ('increase' and 'expansion'). 'facilities' is in the prepositional phrase 'of municipal wastewater treatment facilities'. The singular subject 'expansion' requires the singular verb 'was'."
        ),
        # Q25 Transitions
        (
            DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
            "Quantum entanglement allows pairs of particles to exhibit correlated physical states across arbitrary distances. _____, this phenomenon cannot be harnessed for faster-than-light telecommunication, because measuring one entangled particle produces inherently random outcomes that convey zero decodable information without a classical transmission channel.",
            "Which choice completes the text with the most logical transition?",
            "Nevertheless,",
            ["Furthermore,", "Similarly,", "For instance,"],
            "The passage contrasts the extraordinary feature of instantaneous entanglement across distance with the limitation that it cannot transmit information faster than light, requiring 'Nevertheless'."
        ),
        # Q26 Rhetorical Synthesis
        (
            DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Hard",
            "While researching a topic, a student has taken the following notes:<br><ul style='margin: 8px 0; padding-left: 20px; list-style-type: disc;'><li style='margin-bottom: 4px;'>The Voyager 1 spacecraft was launched by NASA in September 1977.</li><li style='margin-bottom: 4px;'>In August 2012, it crossed the heliopause at a distance of 121 AU (18 billion km) from the Sun.</li><li style='margin-bottom: 4px;'>The heliopause is the boundary where the solar wind is arrested by interstellar gas.</li><li style='margin-bottom: 4px;'>Crossing the heliopause made Voyager 1 the first human-made object to enter interstellar space.</li><li style='margin-bottom: 4px;'>It carries a gold-plated audio-visual phonograph record containing sounds and images of Earth.</li></ul>",
            "The student wants to emphasize the historic milestone Voyager 1 achieved in 2012. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
            "In August 2012, NASA's Voyager 1 achieved a historic milestone by crossing the heliopause 121 AU from the Sun, becoming the first human-made object to venture into interstellar space.",
            [
                "Launched in September 1977, the Voyager 1 space probe was equipped with a gold-plated record carrying sounds and images representing human civilization.",
                "The heliopause, located roughly 18 billion kilometers from the Sun, is the boundary where solar wind meets the interstellar medium.",
                "Voyager 1 traveled for thirty-five years through the solar system before reaching a distance of 121 AU from Earth."
            ],
            "The choice explicitly emphasizes the historic milestone achieved in 2012 (crossing the heliopause and becoming the first human-made object in interstellar space)."
        ),
        # Q27 Words in Context
        (
            DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
            "The economic historian noted that while standard market models assume economic agents possess perfect information and act with relentless rationality, actual financial market behavior is routinely distorted by _____ surges of collective panic and euphoria.",
            "Which choice completes the text with the most logical and precise word or phrase?",
            "capricious", ["circumspect", "pedantic", "inviolable"],
            "'Capricious' means impulsive, erratic, or unpredictable. Surges of collective panic and euphoria are capricious distortions."
        )
    ]

    for i, spec in enumerate(rw_m2_specs):
        target_letter = RW_TARGETS[i]
        if len(spec) == 7:
            domain, subdomain, diff, stim, corr, dists, expl = spec
            prompt = "Which choice most logically completes the text?" if "_____" in stim else "Which finding, if true, most strongly supports the hypothesis?"
        else:
            domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        rw_m2.append(make_hard_mcq(f"t1-rw-m2-q{i+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # =========================================================================
    # TEST 1 - MATH MODULE 1 (Routing Module: Mixed Hard/Medium, Balanced Dist.)
    # =========================================================================
    math_m1_mcqs = [
        # Q1 Linear Equations
        (
            DOMAINS["MATH"]["ALG"], "Linear Equations", "Medium",
            "If $\\frac{3}{4}(8x - 12) + 5 = 2(3x - 1) + k$ has infinitely many solutions, what is the value of $k$?",
            "Which choice is the value of $k$?",
            "-2", ["2", "-4", "4"],
            "Expand the left side: $\\frac{3}{4}(8x) - \\frac{3}{4}(12) + 5 = 6x - 9 + 5 = 6x - 4$. Expand the right side: $2(3x) - 2(1) + k = 6x - 2 + k$. For infinitely many solutions, the constant terms must be equal: $-4 = -2 + k \\implies k = -2$."
        ),
        # Q2 Systems of Linear Equations
        (
            DOMAINS["MATH"]["ALG"], "Systems of Equations", "Medium",
            "In the system of equations below, $c$ is a constant:<br>$$3x - 5y = 14$$<br>$$kx - 15y = 42$$<br>If the system has infinitely many solutions, what is the value of $k$?",
            "Which choice is the value of $k$?",
            "9", ["3", "-9", "15"],
            "Notice that multiplying the first equation $3x - 5y = 14$ by 3 yields $3(3x) - 3(5y) = 3(14) \\implies 9x - 15y = 42$. For the two equations to be identical (infinitely many solutions), we must have $k = 9$."
        ),
        # Q3 Linear Inequalities
        (
            DOMAINS["MATH"]["ALG"], "Linear Inequalities", "Hard",
            "A small business owner manufactures two artisanal desk models: Classic and Executive. The Classic model requires 4 hours of assembly and 2 hours of finishing, yielding a profit of $120. The Executive model requires 5 hours of assembly and 4 hours of finishing, yielding a profit of $180. The workshop has at most 160 assembly hours and at most 100 finishing hours available each month. If the owner manufactures $c$ Classic desks and $e$ Executive desks, which system of inequalities represents all valid production constraints?",
            "Which choice is the correct system of constraints?",
            "$$4c + 5e \\le 160$$<br>$$2c + 4e \\le 100$$<br>$$c \\ge 0, e \\ge 0$$",
            [
                "$$5c + 4e \\le 160$$<br>$$4c + 2e \\le 100$$<br>$$c \\ge 0, e \\ge 0$$",
                "$$4c + 2e \\le 160$$<br>$$5c + 4e \\le 100$$<br>$$c \\ge 0, e \\ge 0$$",
                "$$120c + 180e \\le 160$$<br>$$c + e \\le 100$$<br>$$c \\ge 0, e \\ge 0$$"
            ],
            "Assembly hours required: $4c + 5e \\le 160$. Finishing hours required: $2c + 4e \\le 100$. Also, non-negative quantities $c \\ge 0$ and $e \\ge 0$."
        ),
        # Q4 Quadratic Discriminant
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "For what positive value of $k$ does the quadratic equation $3x^2 - kx + 12 = 0$ have exactly one real solution?",
            "Which choice is the value of $k$?",
            "12", ["6", "18", "144"],
            "A quadratic equation $ax^2 + bx + c = 0$ has exactly one real solution when its discriminant $\\Delta = b^2 - 4ac = 0$. Here, $(-k)^2 - 4(3)(12) = 0 \\implies k^2 - 144 = 0 \\implies k^2 = 144$. Since $k > 0$, $k = 12$."
        ),
        # Q5 Vertex Form & Transformations
        (
            DOMAINS["MATH"]["ADV"], "Nonlinear Functions", "Hard",
            "The parabola $y = -2x^2 + 12x - 13$ is rewritten in vertex form as $y = a(x - h)^2 + k$. What is the value of $a + h + k$?",
            "Which choice is the value?",
            "6", ["8", "10", "4"],
            "Factor $-2$ from the $x$ terms: $y = -2(x^2 - 6x) - 13$. Complete the square inside: $(x - 3)^2 = x^2 - 6x + 9$. So $y = -2(x - 3)^2 + 2(9) - 13 = -2(x - 3)^2 + 18 - 13 = -2(x - 3)^2 + 5$. Thus, $a = -2$, $h = 3$, and $k = 5$. The sum $a + h + k = -2 + 3 + 5 = 6$."
        ),
        # Q6 Exponential Growth & Decay
        (
            DOMAINS["MATH"]["ADV"], "Exponential Functions", "Hard",
            "A pharmaceutical compound has an initial concentration of $240\\text{ mg/L}$ in a patient's bloodstream and degrades exponentially. Every 4.5 hours, the concentration decreases by $35\\%$. Which function $C(t)$ gives the concentration, in $\\text{mg/L}$, remaining $t$ hours after administration?",
            "Which choice correctly models the concentration?",
            "$$C(t) = 240(0.65)^{t / 4.5}$$",
            [
                "$$C(t) = 240(0.35)^{t / 4.5}$$",
                "$$C(t) = 240(0.65)^{4.5t}$$",
                "$$C(t) = 240(1.35)^{t / 4.5}$$"
            ],
            "Decreasing by $35\\%$ means $1 - 0.35 = 0.65$ remains each period. Since this occurs every 4.5 hours, the exponent is $t / 4.5$, yielding $C(t) = 240(0.65)^{t / 4.5}$."
        ),
        # Q7 Polynomial Division & Factor Theorem
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "The polynomial $P(x) = 2x^3 - 5x^2 + kx - 18$ is divisible by $(x - 3)$. What is the value of $k$?",
            "Which choice is the value of $k$?",
            "3", ["-3", "6", "-6"],
            "By the Factor Theorem, if $(x - 3)$ is a factor of $P(x)$, then $P(3) = 0$. Substitute $x = 3$: $P(3) = 2(3)^3 - 5(3)^2 + k(3) - 18 = 2(27) - 5(9) + 3k - 18 = 54 - 45 + 3k - 18 = 3k - 9 = 0 \\implies 3k = 9 \\implies k = 3$."
        ),
        # Q8 Rational Expressions & Asymptotes
        (
            DOMAINS["MATH"]["ADV"], "Rational Functions", "Hard",
            "The rational function $f(x) = \\frac{4x^2 - 16}{2x^2 - 5x - 12}$ has vertical asymptote(s) and a removable discontinuity (hole). At what value of $x$ does the graph of $f$ have a removable discontinuity?",
            "Which choice is the x-value of the hole?",
            "-2", ["-3/2", "4", "2"],
            "Factor numerator: $4(x^2 - 4) = 4(x - 2)(x + 2)$. Factor denominator: $2x^2 - 5x - 12 = (2x + 3)(x - 4)$. Wait! Let's check common factors: $2(-2)^2 - 5(-2) - 12 = 8 + 10 - 12 = 6 \\neq 0$. If numerator is $2x^2 - 8 = 2(x-2)(x+2)$, let's make denominator share $(x - 4)$ or $(x + 2)$! If denominator is $(x - 2)(2x + 5) = 2x^2 + x - 10$, then $x = 2$ is a hole! Let's define $f(x) = \\frac{2x^2 - 8}{x^2 + x - 6} = \\frac{2(x-2)(x+2)}{(x-2)(x+3)}$. The hole is at $x = 2$!"
        ),
        # Q9 Rates and Proportions
        (
            DOMAINS["MATH"]["PSDA"], "Rates and Proportions", "Medium",
            "A high-speed industrial 3D printer prints a polymer gear assembly in 3 hours and 20 minutes. If the printing speed is increased by $25\\%$, how many minutes will it take to print the same gear assembly?",
            "Which choice is the time in minutes?",
            "160 minutes", ["150 minutes", "175 minutes", "180 minutes"],
            "Initial time: 3 hours and 20 minutes $= 200$ minutes. If speed increases by $25\\%$, the new speed is $1.25 \\times \\text{initial speed}$. Time is inversely proportional to speed: $\\text{New time} = \\frac{200}{1.25} = 160$ minutes."
        ),
        # Q10 Percentages and Multi-Step
        (
            DOMAINS["MATH"]["PSDA"], "Percentages", "Medium",
            "A retail electronics store purchased a batch of laptops at wholesale price $W$. The store marked up the wholesale price by $40\\%$ to set the retail sticker price. During a holiday clearance event, the store discounted the sticker price by $25\\%$. What was the final selling price of a laptop in terms of the wholesale price $W$?",
            "Which choice gives the final price?",
            "$1.05W$", ["$1.15W$", "$0.95W$", "$1.10W$"],
            "Sticker price after $40\\%$ markup: $W \\times 1.40 = 1.40W$. Clearance discount of $25\\%$: $1.40W \\times (1 - 0.25) = 1.40W \\times 0.75 = 1.05W$."
        ),
        # Q11 Two-Way Tables & Conditional Probability
        (
            DOMAINS["MATH"]["PSDA"], "Probability", "Hard",
            "A clinical trial evaluated 400 patients testing a diagnostic biomarker for early-stage oncology detection:<br><br><table style='width:100%; border-collapse: collapse; margin: 8px 0; font-size: 13px;'><tr style='background: #f1f5f9;'><th style='border: 1px solid #cbd5e1; padding: 6px;'>Biomarker Test Result</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Condition Present</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Condition Absent</th><th style='border: 1px solid #cbd5e1; padding: 6px;'>Total</th></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Positive Result</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>76</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>24</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>100</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Negative Result</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>4</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>296</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>300</td></tr><tr><td style='border: 1px solid #cbd5e1; padding: 6px;'>Total</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>80</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>320</td><td style='border: 1px solid #cbd5e1; padding: 6px;'>400</td></tr></table><br>Given that a randomly selected patient received a positive test result, what is the probability that the patient actually has the condition present?",
            "Which choice is the probability?",
            "0.76", ["0.95", "0.19", "0.24"],
            "Conditional probability formula: $P(\\text{Condition Present} \\mid \\text{Positive}) = \\frac{\\text{Condition Present and Positive}}{\\text{Total Positive}} = \\frac{76}{100} = 0.76$."
        ),
        # Q12 Margin of Error & Statistics
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "A sociological research organization surveyed a representative random sample of 1,200 adult residents in a metropolitan area and found that $64\\%$ favored expanding municipal light-rail transit, with an associated margin of error of $\\pm 2.8\\%$ at a $95\\%$ confidence level. Which of the following changes to the study design would be guaranteed to reduce the margin of error?",
            "Which choice describes the change?",
            "Increasing the sample size from 1,200 to 4,800 randomly selected residents while keeping the confidence level at 95%",
            [
                "Increasing the confidence level from 95% to 99% with the same sample size of 1,200 residents",
                "Restricting the survey exclusively to registered voters who use public transit daily",
                "Expanding the total population of the metropolitan area through municipal annexation"
            ],
            "The margin of error for a proportion is proportional to $\\frac{1}{\\sqrt{n}}$. Quadrupling the sample size from 1,200 to 4,800 halves the margin of error (reducing it from $\\pm 2.8\\%$ to $\\pm 1.4\\%$)."
        ),
        # Q13 Standard Deviation Comparison
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "Data Set A and Data Set B each contain 50 positive integers. Data Set A has values ranging from 10 to 90, with frequencies distributed uniformly across the entire interval. Data Set B contains 40 values equal to 50, 5 values equal to 48, and 5 values equal to 52. Both datasets have an identical mean of 50. Which statement must be true regarding the standard deviations of the two datasets?",
            "Which statement is true?",
            "The standard deviation of Data Set A is substantially greater than the standard deviation of Data Set B.",
            [
                "The standard deviation of Data Set B is substantially greater than the standard deviation of Data Set A.",
                "The standard deviations of Data Set A and Data Set B are exactly equal because both datasets have a mean of 50.",
                "It is impossible to compare standard deviations without knowing the exact sum of squared residuals."
            ],
            "Standard deviation measures the average spread of data values from their mean. In Set B, 80% of data is exactly at the mean (50) and the rest is within 2 units, whereas in Set A values spread uniformly across 10 to 90. Thus, Set A has a far greater standard deviation."
        ),
        # Q14 Scatterplots & Nonlinear Best Fit
        (
            DOMAINS["MATH"]["PSDA"], "Scatterplots", "Medium",
            "A research laboratory recorded the cooling of a molten alloy ingot over time. The scatterplot of temperature $T$ (°C) versus elapsed time $t$ (minutes) is modeled by the equation $T = 850(0.92)^t + 25$. What is the best interpretation of the number 25 in this context?",
            "Which choice is the best interpretation?",
            "The ambient room temperature toward which the alloy ingot asymptotically cools",
            [
                "The initial temperature of the molten alloy ingot at time t = 0",
                "The number of minutes required for the ingot to decrease its temperature by half",
                "The average rate of temperature decrease per minute over the first hour"
            ],
            "As $t \\to \\infty$, the exponential term $(0.92)^t \\to 0$, leaving $T \\to 25$°C. Thus, 25 represents the ambient room temperature asymptote."
        ),
        # Q15 Circle Equations & Completing the Square
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "In the xy-plane, the equation of a circle is $x^2 + y^2 - 8x + 10y - 8 = 0$. What are the coordinates of the center $(h, k)$ and the radius $r$ of this circle?",
            "Which choice gives the center and radius?",
            "Center $(4, -5)$ and radius $7$",
            [
                "Center $(-4, 5)$ and radius $7$",
                "Center $(4, -5)$ and radius $49$",
                "Center $(-8, 10)$ and radius $\\sqrt{8}$"
            ],
            "Group terms: $(x^2 - 8x) + (y^2 + 10y) = 8$. Complete squares: $(x - 4)^2 + (y + 5)^2 = 8 + 16 + 25 = 49$. The center is $(4, -5)$ and the radius is $\\sqrt{49} = 7$."
        ),
        # Q16 Right Triangle Trigonometry & Complementary Angles
        (
            DOMAINS["MATH"]["GEOM"], "Trigonometry", "Hard",
            "In a right triangle $ABC$, the measure of $\\angle C = 90^\\circ$. If $\\sin(A) = \\frac{7}{25}$, what is the value of $\\cos(B)$?",
            "Which choice is the value of $\\cos(B)$?",
            "$$\\frac{7}{25}$$",
            ["$$\\frac{24}{25}$$", "$$\\frac{7}{24}$$", "$$\\frac{25}{7}$$"],
            "In any right triangle where $C = 90^\\circ$, angles $A$ and $B$ are complementary: $A + B = 90^\\circ$. By the cofunction identity, $\\cos(B) = \\sin(90^\\circ - B) = \\sin(A) = \\frac{7}{25}$."
        ),
        # Q17 Arc Length & Radians
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle in the xy-plane with center at the origin has a radius of 18 cm. A central angle $\\theta$ measures $\\frac{5\\pi}{6}$ radians. What is the perimeter, in centimeters, of the circular sector subtended by angle $\\theta$?",
            "Which choice is the perimeter?",
            "$$15\\pi + 36$$",
            ["$$15\\pi$$", "$$30\\pi + 36$$", "$$135\\pi + 18$$"],
            "The arc length of the sector is $s = r\\theta = 18 \\times \\frac{5\\pi}{6} = 15\\pi\\text{ cm}$. The perimeter of a sector includes the arc length PLUS two radii bounding the sector: $\\text{Perimeter} = s + 2r = 15\\pi + 2(18) = 15\\pi + 36\\text{ cm}$."
        ),
        # Q18 Similar Triangles & Altitude to Hypotenuse
        (
            DOMAINS["MATH"]["GEOM"], "Triangles", "Hard",
            "In right triangle $XYZ$, $\\angle Y = 90^\\circ$. An altitude $YW$ is drawn to the hypotenuse $XZ$. If $XW = 4$ and $WZ = 9$, what is the length of altitude $YW$?",
            "Which choice is the length of $YW$?",
            "6", ["6.5", "$$\\sqrt{13}$$", "36"],
            "By the Geometric Mean Theorem (Altitude Rule) for right triangles: $YW^2 = XW \\times WZ$. Here, $YW^2 = 4 \\times 9 = 36 \\implies YW = \\sqrt{36} = 6$."
        ),
        # Q19 3D Geometry: Volume & Ratio
        (
            DOMAINS["MATH"]["GEOM"], "Volume", "Hard",
            "A solid bronze cone has a base radius of 6 cm and a height of 15 cm. The cone is melted down and completely recast into a solid sphere with no loss of bronze. What is the radius, in centimeters, of the recast bronze sphere?",
            "Which choice is the radius of the sphere?",
            "$$3\\sqrt[3]{5}$$",
            ["$$\\sqrt[3]{45}$$", "5", "6"],
            "Wait! Volume of cone: $V_c = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi (6^2)(15) = \\frac{1}{3}\\pi(36)(15) = 180\\pi$. Volume of sphere: $V_s = \\frac{4}{3}\\pi R^3$. Equating: $\\frac{4}{3}\\pi R^3 = 180\\pi \\implies R^3 = 180 \\times \\frac{3}{4} = 135$. Radius $R = \\sqrt[3]{135} = \\sqrt[3]{27 \\times 5} = 3\\sqrt[3]{5}$."
        ),
        # Q20 Radical Equations & Extraneous Solutions
        (
            DOMAINS["MATH"]["ADV"], "Radicals", "Hard",
            "What is the solution set of real numbers for the equation $\\sqrt{4x + 17} = x + 3$?",
            "Which choice is the solution set?",
            "$$\\{1\\}$$",
            ["$$\\{-8, 1\\}$$", "$$\\{-8\\}$$", "$$\\emptyset$$"],
            "Square both sides: $4x + 17 = (x + 3)^2 = x^2 + 6x + 9$. Rearrange: $x^2 + 2x - 8 = 0 \\implies (x + 4)(x - 2) = 0 \\implies x = 2$ or $x = -4$! Wait: let's verify with $\\sqrt{4x + 17} = x + 3$: if $x = 1$, $\\sqrt{4(1)+17} = \\sqrt{21} \\neq 4$! Let's make the numbers clean: $\\sqrt{2x + 7} = x - 4$. Square: $2x + 7 = x^2 - 8x + 16 \\implies x^2 - 10x + 9 = 0 \\implies (x - 9)(x - 1) = 0$. Test $x = 1$: $\\sqrt{9} = 3 \\neq 1 - 4 = -3$ (extraneous!). Test $x = 9$: $\\sqrt{25} = 5 = 9 - 4 = 5$ (valid!). Solution set is $\\{9\\}$!"
        ),
        # Q21 Vieta's Formulas & Quadratic Roots
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "The quadratic equation $2x^2 - 7x + 4 = 0$ has real roots $r_1$ and $r_2$. What is the value of $r_1^2 + r_2^2$?",
            "Which choice is the value?",
            "$$\\frac{33}{4}$$",
            ["$$\\frac{49}{4}$$", "$$\\frac{17}{4}$$", "$$\\frac{41}{4}$$"],
            "By Vieta's formulas, $r_1 + r_2 = \\frac{7}{2}$ and $r_1 r_2 = \\frac{4}{2} = 2$. Using the identity $r_1^2 + r_2^2 = (r_1 + r_2)^2 - 2r_1 r_2 = \\left(\\frac{7}{2}\\right)^2 - 2(2) = \\frac{49}{4} - 4 = \\frac{49 - 16}{4} = \\frac{33}{4}$."
        ),
        # Q22 Absolute Value Equations
        (
            DOMAINS["MATH"]["ALG"], "Linear Equations", "Hard",
            "What is the sum of all distinct real solutions to the equation $|2x - 5| = 3x - 10$?",
            "Which choice is the sum?",
            "5", ["8", "3", "7"],
            "Case 1: $2x - 5 = 3x - 10 \\implies -x = -5 \\implies x = 5$. Check $x = 5$: $|2(5) - 5| = |5| = 5$. Right side: $3(5) - 10 = 5$ (Valid). Case 2: $2x - 5 = -(3x - 10) = -3x + 10 \\implies 5x = 15 \\implies x = 3$. Check $x = 3$: $|2(3) - 5| = |-1| = 1$. Right side: $3(3) - 10 = -1$. But absolute value cannot equal $-1$, so $x = 3$ is extraneous! The only real solution is $x = 5$."
        )
    ]

    for i, spec in enumerate(math_m1_mcqs):
        target_letter = MATH_TARGETS[i]
        domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        # Handle Q8 and Q20 custom numbers
        if i == 7: # Q8
            stim = "The rational function $f(x) = \\frac{2x^2 - 8}{x^2 + x - 6}$ has a removable discontinuity (hole) at what value of $x$?"
            corr = "2"
            dists = ["-3", "-2", "4"]
            expl = "Factor numerator: $2(x - 2)(x + 2)$. Factor denominator: $(x - 2)(x + 3)$. The common factor $(x - 2)$ cancels, creating a removable discontinuity at $x = 2$."
        elif i == 19: # Q20
            stim = "What is the solution set of real numbers for the equation $\\sqrt{2x + 7} = x - 4$?"
            corr = "{9}"
            dists = ["{1, 9}", "{1}", "No real solutions"]
            expl = "Square both sides: $2x + 7 = (x - 4)^2 = x^2 - 8x + 16 \\implies x^2 - 10x + 9 = 0 \\implies (x - 9)(x - 1) = 0$. Test $x = 1$: $\\sqrt{9} = 3 \\neq -3$ (extraneous). Test $x = 9$: $\\sqrt{25} = 5 = 9 - 4$ (valid). Solution set is {9}."
        math_m1.append(make_hard_mcq(f"t1-math-m1-q{i+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # Math M1 SPRs (Q23-Q27)
    math_m1_sprs = [
        # Q23 SPR (Linear Systems)
        (
            DOMAINS["MATH"]["ALG"], "Systems of Equations", "Medium",
            "In the system of equations below:<br>$$4x + 3y = 31$$<br>$$2x - y = 3$$<br>What is the value of $x + y$?",
            "Enter the exact integer value of $x + y$:",
            ["11"],
            "From the second equation, $y = 2x - 3$. Substitute into the first: $4x + 3(2x - 3) = 31 \\implies 4x + 6x - 9 = 31 \\implies 10x = 40 \\implies x = 4$. Then $y = 2(4) - 3 = 5$. Thus, $x + y = 4 + 5 = 11$."
        ),
        # Q24 SPR (Polynomial remainder)
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "When the polynomial $P(x) = 3x^3 - 5x^2 + 8x + c$ is divided by $(x - 2)$, the remainder is 26. What is the value of constant $c$?",
            "Enter the exact integer value of $c$:",
            ["6"],
            "By the Remainder Theorem, $P(2) = 26$. Substitute $x = 2$: $P(2) = 3(2)^3 - 5(2)^2 + 8(2) + c = 3(8) - 5(4) + 16 + c = 24 - 20 + 16 + c = 20 + c = 26 \\implies c = 6$."
        ),
        # Q25 SPR (Geometry: Special Right Triangles)
        (
            DOMAINS["MATH"]["GEOM"], "Right Triangles", "Hard",
            "In a $30^\\circ-60^\\circ-90^\\circ$ triangle, the hypotenuse has length 16. What is the area of this triangle expressed in the form $a\\sqrt{3}$? Enter the integer value of $a$:",
            "Enter the integer value of $a$:",
            ["32"],
            "In a $30^\\circ-60^\\circ-90^\\circ$ triangle with hypotenuse 16: short leg $= 16 / 2 = 8$, long leg $= 8\\sqrt{3}$. Area $= \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 8 \\times 8\\sqrt{3} = 32\\sqrt{3}$. Therefore, $a = 32$."
        ),
        # Q26 SPR (Algebra: Fractional Exponents)
        (
            DOMAINS["MATH"]["ADV"], "Exponents and Radicals", "Hard",
            "If $27^{2x - 1} = 9^{x + 4}$, what is the value of $x$?",
            "Enter the exact fractional or decimal value of $x$:",
            ["11/4", "2.75"],
            "Rewrite with common base 3: $(3^3)^{2x - 1} = (3^2)^{x + 4} \\implies 3^{6x - 3} = 3^{2x + 8}$. Equate exponents: $6x - 3 = 2x + 8 \\implies 4x = 11 \\implies x = 11/4 = 2.75$."
        ),
        # Q27 SPR (PSDA: Conditional Probability)
        (
            DOMAINS["MATH"]["PSDA"], "Probability", "Hard",
            "A quality control engineer inspects a batch of 80 microchips. 48 chips were produced by Machine A and 32 chips were produced by Machine B. 6 of the chips from Machine A are defective, and 2 of the chips from Machine B are defective. If a randomly selected chip from the batch is found to be defective, what is the probability that it was produced by Machine A? Express your answer as a simplified fraction $\\frac{a}{b}$:",
            "Enter the exact fraction a/b (e.g. 3/4):",
            ["3/4", "0.75"],
            "Total defective chips $= 6 + 2 = 8$. Defective chips from Machine A $= 6$. The conditional probability is $P(\\text{Machine A} \\mid \\text{Defective}) = \\frac{6}{8} = \\frac{3}{4} = 0.75$."
        )
    ]

    for j, spec in enumerate(math_m1_sprs):
        domain, subdomain, diff, stim, prompt, answers, expl = spec
        math_m1.append(make_spr(f"t1-math-m1-q{j+23}", domain, subdomain, diff, stim, prompt, answers, expl))

    # =========================================================================
    # TEST 1 - MATH MODULE 2 (Adaptive Hard Module: Rigorous 750-800 Level)
    # =========================================================================
    math_m2_mcqs = [
        # Q1 Systems with Parameters
        (
            DOMAINS["MATH"]["ALG"], "Systems of Equations", "Hard",
            "In the system of equations below, $a$ and $b$ are constants:<br>$$ax + 6y = 18$$<br>$$4x + by = 12$$<br>If the system has no solution, which equation must be true?",
            "Which choice must be true?",
            "$$ab = 24\\text{ and }a \\neq 6$$",
            [
                "$$ab = 24\\text{ and }a = 6$$",
                "$$ab = 72$$",
                "$$a + b = 10$$"
            ],
            "For a system to have no solution, lines must be parallel with different intercepts: $\\frac{a}{4} = \\frac{6}{b} \\neq \\frac{18}{12}$. From $\\frac{a}{4} = \\frac{6}{b}$, we get $ab = 24$. From $\\frac{a}{4} \\neq \\frac{18}{12} = \\frac{3}{2}$, we get $a \\neq 6$."
        ),
        # Q2 Absolute Value Inequality
        (
            DOMAINS["MATH"]["ALG"], "Inequalities", "Hard",
            "What is the complete set of solutions to the inequality $|3x - 7| + 4 \\le 19$?",
            "Which choice is the solution set?",
            "$$-\\frac{8}{3} \\le x \\le \\frac{22}{3}$$",
            [
                "$$x \\le \\frac{22}{3}$$",
                "$$-\\frac{22}{3} \\le x \\le \\frac{8}{3}$$",
                "$$x \\ge -\\frac{8}{3}$$"
            ],
            "Subtract 4 from both sides: $|3x - 7| \\le 15$. This unfolds into the compound inequality: $-15 \\le 3x - 7 \\le 15$. Add 7: $-8 \\le 3x \\le 22$. Divide by 3: $-\\frac{8}{3} \\le x \\le \\frac{22}{3}$."
        ),
        # Q3 Perpendicular Lines with Fractional Intercepts
        (
            DOMAINS["MATH"]["ALG"], "Linear Functions", "Hard",
            "Line $L_1$ passes through the points $(-3, 8)$ and $(6, -4)$. Line $L_2$ is perpendicular to line $L_1$ and passes through the point $(4, 1)$. What is the y-intercept of line $L_2$?",
            "Which choice is the y-intercept?",
            "-2", ["-5", "4", "2"],
            "Slope of $L_1$: $m_1 = \\frac{-4 - 8}{6 - (-3)} = \\frac{-12}{9} = -\\frac{4}{3}$. Perpendicular slope $m_2 = -\\frac{1}{m_1} = \\frac{3}{4}$. Line $L_2$ in point-slope form: $y - 1 = \\frac{3}{4}(x - 4) \\implies y - 1 = \\frac{3}{4}x - 3 \\implies y = \\frac{3}{4}x - 2$. The y-intercept is -2."
        ),
        # Q4 Quadratic Discriminant & Line Tangency
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "A line with equation $y = mx - 5$ is tangent to the parabola $y = 2x^2 + 8x + 3$ at exactly one point. What is the product of all possible values of $m$?",
            "Which choice is the product of all possible values of $m$?",
            "0", ["64", "-64", "16"],
            "Set the equations equal: $2x^2 + 8x + 3 = mx - 5 \\implies 2x^2 + (8 - m)x + 8 = 0$. For tangency (exactly one intersection), discriminant $\\Delta = 0$: $(8 - m)^2 - 4(2)(8) = 0 \\implies (8 - m)^2 - 64 = 0 \\implies (8 - m)^2 = 64$. Thus, $8 - m = 8 \\implies m = 0$, or $8 - m = -8 \\implies m = 16$. The product of all possible values of $m$ is $0 \\times 16 = 0$."
        ),
        # Q5 Vertex Optimization & Revenue Model
        (
            DOMAINS["MATH"]["ADV"], "Nonlinear Modeling", "Hard",
            "A software company models its monthly subscription revenue $R(p)$, in thousands of dollars, as a function of the price per user $p$, in dollars: $R(p) = -0.5p^2 + 42p - 280$. What subscription price $p$ maximizes the company's monthly revenue, and what is that maximum monthly revenue?",
            "Which choice gives the optimal price and maximum revenue?",
            "Price: $42; Maximum Revenue: $602 thousand",
            [
                "Price: $84; Maximum Revenue: $1,204 thousand",
                "Price: $42; Maximum Revenue: $280 thousand",
                "Price: $21; Maximum Revenue: $504 thousand"
            ],
            "The vertex of a parabola $y = ap^2 + bp + c$ occurs at $p = -\\frac{b}{2a} = -\\frac{42}{2(-0.5)} = \\frac{42}{1} = 42$. Maximum revenue: $R(42) = -0.5(42)^2 + 42(42) - 280 = -0.5(1764) + 1764 - 280 = -882 + 1764 - 280 = 882 - 280 = 602$ thousand dollars."
        ),
        # Q6 Polynomial Remainder & Multi-Condition
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "The polynomial $P(x) = x^4 - 2x^3 + ax^2 + bx - 12$ has $(x - 2)$ as a factor, and when $P(x)$ is divided by $(x + 1)$, the remainder is 18. What is the value of $a - b$?",
            "Which choice is the value of $a - b$?",
            "-7", ["7", "11", "-11"],
            "Condition 1: $P(2) = 0 \\implies 16 - 16 + 4a + 2b - 12 = 0 \\implies 4a + 2b = 12 \\implies 2a + b = 6$. Condition 2: $P(-1) = 18 \\implies 1 + 2 + a - b - 12 = 18 \\implies a - b - 9 = 18 \\implies a - b = 27$! Let's check: if $2a + b = 6$ and $a - b = 27$, then add: $3a = 33 \\implies a = 11$, and $b = 6 - 2(11) = -16$. Then $a - b = 11 - (-16) = 27$!"
        ),
        # Q7 Rational Functions: Oblique & Horizontal Asymptotes
        (
            DOMAINS["MATH"]["ADV"], "Rational Functions", "Hard",
            "Which of the following lines is the horizontal asymptote of the rational function $g(x) = \\frac{6x^3 - 5x + 14}{2x^3 + 7x^2 - 9}$?",
            "Which choice is the equation of the horizontal asymptote?",
            "$$y = 3$$",
            ["$$y = 0$$", "$$y = 6$$", "No horizontal asymptote exists"],
            "Both numerator and denominator have equal degree 3. The horizontal asymptote is the ratio of leading coefficients: $y = \\frac{6}{2} = 3$."
        ),
        # Q8 Exponential Decay Half-Life Unit Conversion
        (
            DOMAINS["MATH"]["ADV"], "Exponential Functions", "Hard",
            "A radioactive isotope has a half-life of 28 days. A sample initially contains 800 grams of the isotope. Which expression represents the amount, in grams, of the isotope remaining after $d$ days, where the decay factor is expressed per single day?",
            "Which choice is the expression?",
            "$$800\\left(\\frac{1}{2}\\right)^{d / 28}$$",
            [
                "$$800\\left(\\frac{1}{56}\\right)^d$$",
                "$$800\\left(28\\right)^{-d/2}$$",
                "$$800\\left(\\frac{1}{2}\\right)^{28d}$$"
            ],
            "With half-life $T = 28$ days, the base is $1/2$ and the number of elapsed half-lives in $d$ days is $d / 28$. Thus, $A(d) = 800\\left(\\frac{1}{2}\\right)^{d / 28}$."
        ),
        # Q9 Radical and Extraneous
        (
            DOMAINS["MATH"]["ADV"], "Radicals", "Hard",
            "What is the sum of all real values of $x$ that satisfy $\\sqrt{3x + 19} - x = 1$?",
            "Which choice is the sum?",
            "3", ["-3", "2", "-2"],
            "Isolate the radical: $\\sqrt{3x + 19} = x + 1$. Square both sides: $3x + 19 = x^2 + 2x + 1 \\implies x^2 - x - 18 = 0$. Roots: $x = \\frac{1 \\pm \\sqrt{1 + 72}}{2} = \\frac{1 \\pm \\sqrt{73}}{2}$. Since $\\sqrt{73} \\approx 8.54$, $\\frac{1 - 8.54}{2} \\approx -3.77$ would make $x + 1 < 0$, which cannot equal a principal square root! Let's choose integers: $\\sqrt{3x + 10} - x = 2 \\implies \\sqrt{3x + 10} = x + 2 \\implies 3x + 10 = x^2 + 4x + 4 \\implies x^2 + x - 6 = 0 \\implies (x + 3)(x - 2) = 0$. For $x = -3$: $x + 2 = -1 < 0$ (extraneous). For $x = 2$: $\\sqrt{16} = 4 = 2 + 2$ (valid). Thus $x = 2$."
        ),
        # Q10 Two-Variable Optimization / Linear System
        (
            DOMAINS["MATH"]["ALG"], "Linear Modeling", "Hard",
            "A civil engineering contractor mixes two grades of concrete aggregate: Aggregate X containing $15\\%$ silica and Aggregate Y containing $40\\%$ silica. The contractor requires 50 tons of an aggregate mix containing exactly $25\\%$ silica. How many tons of Aggregate X must be used in the mixture?",
            "Which choice is the tons of Aggregate X?",
            "30 tons", ["20 tons", "25 tons", "35 tons"],
            "Let $x$ be tons of X and $y$ be tons of Y. System: $x + y = 50$, and $0.15x + 0.40y = 0.25(50) = 12.5$. Substitute $y = 50 - x$: $0.15x + 0.40(50 - x) = 12.5 \\implies 0.15x + 20 - 0.40x = 12.5 \\implies -0.25x = -7.5 \\implies x = 30$ tons."
        ),
        # Q11 Scatterplot & Residual Analysis
        (
            DOMAINS["MATH"]["PSDA"], "Scatterplots", "Hard",
            "An environmental scientist records particulate air pollution levels $y$ (in $\\mu\\text{g/m}^3$) and wind speed $x$ (in km/h). The linear line of best fit is $\\hat{y} = -2.4x + 85$. For a wind speed of 15 km/h, the actual measured pollution was $52\\,\\mu\\text{g/m}^3$. What was the residual for this data point?",
            "Which choice is the residual?",
            "3", ["-3", "49", "52"],
            "Predicted value $\\hat{y} = -2.4(15) + 85 = -36 + 85 = 49$. The residual is defined as $\\text{Actual} - \\text{Predicted} = 52 - 49 = 3$."
        ),
        # Q12 Conditional Probability with Percentages
        (
            DOMAINS["MATH"]["PSDA"], "Probability", "Hard",
            "In an aerodynamic manufacturing facility, $60\\%$ of components are manufactured by Robotic Line 1 and $40\\%$ by Robotic Line 2. Historical audit records show that $2\\%$ of components from Line 1 are defective, whereas $5\\%$ of components from Line 2 are defective. If a randomly selected component is inspected and found to be defective, what is the probability that it was produced by Robotic Line 2?",
            "Which choice is the probability?",
            "$$\\frac{5}{8}$$",
            ["$$\\frac{3}{8}$$", "$$\\frac{2}{5}$$", "$$\\frac{4}{7}$$"],
            "Total probability of defective: $P(D) = (0.60)(0.02) + (0.40)(0.05) = 0.012 + 0.020 = 0.032$. By Bayes' Theorem: $P(\\text{Line 2} \\mid D) = \\frac{P(\\text{Line 2} \\cap D)}{P(D)} = \\frac{0.020}{0.032} = \\frac{20}{32} = \\frac{5}{8}$."
        ),
        # Q13 Box Plots & Interquartile Range
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "A pharmaceutical researcher compares the distribution of patient recovery times for Treatment A and Treatment B. Both distributions have 100 observations. Treatment A has a minimum of 4 days, $Q_1 = 8$, median $= 12$, $Q_3 = 18$, and maximum $= 26$. Treatment B has a minimum of 6 days, $Q_1 = 11$, median $= 15$, $Q_3 = 17$, and maximum $= 28$. Which of the following statements must be true?",
            "Which statement must be true?",
            "The interquartile range of Treatment A is greater than the interquartile range of Treatment B.",
            [
                "The range of Treatment B is greater than the range of Treatment A.",
                "At least 50% of patients in Treatment A had a longer recovery time than the median of Treatment B.",
                "The mean recovery time for Treatment B is guaranteed to be greater than 15 days."
            ],
            "Interquartile Range (IQR) $= Q_3 - Q_1$. For Treatment A: $\\text{IQR} = 18 - 8 = 10$. For Treatment B: $\\text{IQR} = 17 - 11 = 6$. Thus, the IQR of Treatment A (10) is greater than that of Treatment B (6)."
        ),
        # Q14 Normal Distribution & Empirical Rule
        (
            DOMAINS["MATH"]["PSDA"], "Data Distributions", "Hard",
            "The distribution of scores on a national certification exam is approximately normal with a mean of $\\mu = 520$ and a standard deviation of $\\sigma = 60$. Approximately what percentage of test-takers scored between 400 and 580?",
            "Which choice is the approximate percentage?",
            "81.5%", ["68%", "95%", "84%"],
            "Standard scores: $z_1 = \\frac{400 - 520}{60} = -2.0$, and $z_2 = \\frac{580 - 520}{60} = +1.0$. By the empirical rule, between $\\mu - 2\\sigma$ and $\\mu$ is $\\approx 47.5\\%$. Between $\\mu$ and $\\mu + 1\\sigma$ is $\\approx 34\\%$. Total percentage $= 47.5\\% + 34\\% = 81.5\\%$."
        ),
        # Q15 Circle Tangent & Line Intersection
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "In the xy-plane, the circle $(x - 3)^2 + (y + 4)^2 = 25$ is tangent to line $k$ at the point $(6, 0)$. What is the slope of tangent line $k$?",
            "Which choice is the slope of line $k$?",
            "$$-\\frac{3}{4}$$",
            ["$$\\frac{4}{3}$$", "$$-\\frac{4}{3}$$", "$$\\frac{3}{4}$$"],
            "Center of circle is $C(3, -4)$. Point of tangency is $P(6, 0)$. Slope of radius $CP = \\frac{0 - (-4)}{6 - 3} = \\frac{4}{3}$. The tangent line is perpendicular to the radius at the point of tangency, so its slope is $m = -\\frac{1}{4/3} = -\\frac{3}{4}$."
        ),
        # Q16 Arc Length & Inscribed Angles
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "In a circle with radius 12, inscribed angle $\\angle ABC$ intercepts an arc $AC$. If the measure of $\\angle ABC = 45^\\circ$, what is the length of minor arc $AC$?",
            "Which choice is the arc length?",
            "$$6\\pi$$",
            ["$$12\\pi$$", "$$3\\pi$$", "$$9\\pi$$"],
            "The central angle subtending arc $AC$ is twice the inscribed angle: $\\theta = 2 \\times 45^\\circ = 90^\\circ = \\frac{\\pi}{2}$ radians. Arc length $s = r\\theta = 12 \\times \\frac{\\pi}{2} = 6\\pi$."
        ),
        # Q17 Trigonometric Identities: sin^2 + cos^2
        (
            DOMAINS["MATH"]["GEOM"], "Trigonometry", "Hard",
            "In right triangle $DEF$ with right angle at $E$, if $\\tan(D) = \\frac{5}{12}$, what is the value of $\\sin(D) + \\cos(D)$?",
            "Which choice is the value?",
            "$$\\frac{17}{13}$$",
            ["$$\\frac{12}{13}$$", "$$\\frac{7}{13}$$", "$$\\frac{13}{12}$$"],
            "With $\\tan(D) = 5/12$, opposite side $= 5$ and adjacent side $= 12$. Hypotenuse $= \\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13$. Thus, $\\sin(D) = 5/13$ and $\\cos(D) = 12/13$. Sum $= 5/13 + 12/13 = 17/13$."
        ),
        # Q18 Radians & Complementary Angles
        (
            DOMAINS["MATH"]["GEOM"], "Trigonometry", "Hard",
            "In the xy-plane, an acute angle $\\theta$ satisfies $\\sin(\\theta) = \\cos\\left(\\frac{3\\pi}{8}\\right)$. What is the measure of angle $\\theta$ in radians?",
            "Which choice is the measure of $\\theta$?",
            "$$\\frac{\\pi}{8}$$",
            ["$$\\frac{3\\pi}{8}$$", "$$\\frac{\\pi}{4}$$", "$$\\frac{5\\pi}{8}$$"],
            "By the cofunction identity in radians, $\\sin(\\theta) = \\cos\\left(\\frac{\\pi}{2} - \\theta\\right)$. Equating arguments: $\\frac{\\pi}{2} - \\theta = \\frac{3\\pi}{8} \\implies \\theta = \\frac{\\pi}{2} - \\frac{3\\pi}{8} = \\frac{4\\pi - 3\\pi}{8} = \\frac{\\pi}{8}$."
        ),
        # Q19 Density & 3D Geometry
        (
            DOMAINS["MATH"]["GEOM"], "Density", "Hard",
            "A solid cylindrical copper rod has a diameter of 4 cm and a length of 50 cm. The density of copper is $8.96\\text{ g/cm}^3$. What is the mass of the rod in kilograms, rounded to the nearest tenth of a kilogram?",
            "Which choice is the mass in kilograms?",
            "5.6 kg", ["22.5 kg", "11.3 kg", "2.8 kg"],
            "Radius $r = 4 / 2 = 2$ cm, height $h = 50$ cm. Volume $V = \\pi r^2 h = \\pi (2^2)(50) = 200\\pi\\text{ cm}^3 \\approx 200(3.14159) = 628.32\\text{ cm}^3$. Mass $= V \\times \\text{density} = 628.32 \\times 8.96 \\approx 5630\\text{ g} = 5.63\\text{ kg} \\approx 5.6\\text{ kg}$."
        ),
        # Q20 Polynomial Vieta's 3rd Degree
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "The cubic equation $x^3 - 6x^2 + 11x - 6 = 0$ has three real roots $p, q,$ and $r$. What is the value of $\\frac{1}{p} + \\frac{1}{q} + \\frac{1}{r}$?",
            "Which choice is the value?",
            "$$\\frac{11}{6}$$",
            ["$$\\frac{6}{11}$$", "1", "6"],
            "Combine fractions: $\\frac{1}{p} + \\frac{1}{q} + \\frac{1}{r} = \\frac{pq + pr + qr}{pqr}$. By Vieta's formulas for $x^3 + bx^2 + cx + d = 0$: $pq + pr + qr = c = 11$, and $pqr = -d = -(-6) = 6$. Thus, the value is $\\frac{11}{6}$."
        ),
        # Q21 Circle Chord Length
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle with radius 10 has a chord $AB$ situated at a perpendicular distance of 6 units from the center of the circle. What is the length of chord $AB$?",
            "Which choice is the length of chord $AB$?",
            "16", ["8", "12", "$$4\\sqrt{34}$$"],
            "The perpendicular from the center to the chord bisects the chord and forms a right triangle with the radius as hypotenuse: $r = 10$, distance $d = 6$. Half-chord length $= \\sqrt{10^2 - 6^2} = \\sqrt{100 - 36} = \\sqrt{64} = 8$. Full chord length $= 2 \\times 8 = 16$."
        ),
        # Q22 Rational Function Hole & Coordinates
        (
            DOMAINS["MATH"]["ADV"], "Rational Functions", "Hard",
            "The function $h(x) = \\frac{3x^2 - 12x}{x^2 - 16}$ has a removable discontinuity (hole) at point $(x_0, y_0)$. What is the value of $y_0$?",
            "Which choice is the y-coordinate of the hole?",
            "$$\\frac{3}{2}$$",
            ["$$\\frac{3}{4}$$", "3", "0"],
            "Factor: $h(x) = \\frac{3x(x - 4)}{(x - 4)(x + 4)}$. The hole occurs at $x = 4$. For $x \\neq 4$, simplified function is $h^*(x) = \\frac{3x}{x + 4}$. Substitute $x = 4$: $y_0 = \\frac{3(4)}{4 + 4} = \\frac{12}{8} = \\frac{3}{2}$."
        )
    ]

    for k, spec in enumerate(math_m2_mcqs):
        target_letter = MATH_TARGETS[k]
        domain, subdomain, diff, stim, prompt, corr, dists, expl = spec
        # Handle Q6 and Q9
        if k == 5: # Q6
            stim = "The polynomial $P(x) = x^4 - 2x^3 + ax^2 + bx - 12$ has $(x - 2)$ as a factor, and when $P(x)$ is divided by $(x + 1)$, the remainder is 18. What is the value of $a - b$?"
            corr = "27"
            dists = ["11", "-7", "18"]
            expl = "Condition 1: $P(2) = 0 \\implies 16 - 16 + 4a + 2b - 12 = 0 \\implies 4a + 2b = 12 \\implies 2a + b = 6$. Condition 2: $P(-1) = 18 \\implies 1 + 2 + a - b - 12 = 18 \\implies a - b = 27$."
        elif k == 8: # Q9
            stim = "What is the unique real solution to the equation $\\sqrt{3x + 10} - x = 2$?"
            corr = "2"
            dists = ["-3", "4", "No real solution"]
            expl = "Isolate radical: $\\sqrt{3x + 10} = x + 2$. Square: $3x + 10 = x^2 + 4x + 4 \\implies x^2 + x - 6 = 0 \\implies (x + 3)(x - 2) = 0$. For $x = -3$, $x + 2 = -1 < 0$ (extraneous). For $x = 2$, $\\sqrt{16} = 4 = 2 + 2$ (valid). Solution is 2."
        math_m2.append(make_hard_mcq(f"t1-math-m2-q{k+1}", domain, subdomain, diff, stim, prompt, corr, dists, target_letter, expl))

    # Math M2 SPRs (Q23-Q27)
    math_m2_sprs = [
        # Q23 SPR (Nonlinear System Tangency)
        (
            DOMAINS["MATH"]["ADV"], "Quadratic Equations", "Hard",
            "The line $y = 4x + c$ intersects the parabola $y = x^2 - 6x + 30$ at exactly one point in the xy-plane. What is the value of constant $c$?",
            "Enter the exact integer value of c:",
            ["5"],
            "Set equations equal: $x^2 - 6x + 30 = 4x + c \\implies x^2 - 10x + (30 - c) = 0$. For exactly one intersection, discriminant $\\Delta = 0$: $(-10)^2 - 4(1)(30 - c) = 0 \\implies 100 - 120 + 4c = 0 \\implies -20 + 4c = 0 \\implies 4c = 20 \\implies c = 5$."
        ),
        # Q24 SPR (Polynomial Vieta Product)
        (
            DOMAINS["MATH"]["ADV"], "Polynomials", "Hard",
            "In the polynomial function $f(x) = (x - 4)(x + 2)(2x - 7)$, what is the y-intercept of the graph of $y = f(x)$ in the xy-plane?",
            "Enter the exact integer value of the y-intercept:",
            ["56"],
            "The y-intercept occurs where $x = 0$. Substitute $x = 0$: $f(0) = (0 - 4)(0 + 2)(2(0) - 7) = (-4)(2)(-7) = 56$."
        ),
        # Q25 SPR (Circle Completing Square & Radius)
        (
            DOMAINS["MATH"]["GEOM"], "Circles", "Hard",
            "A circle in the xy-plane has equation $2x^2 + 2y^2 - 12x + 16y - 30 = 0$. What is the radius of the circle?",
            "Enter the exact integer value of the radius:",
            ["6"],
            "Divide entire equation by 2: $x^2 + y^2 - 6x + 8y - 15 = 0$. Group terms: $(x^2 - 6x) + (y^2 + 8y) = 15$. Complete squares: $(x - 3)^2 + (y + 4)^2 = 15 + 9 + 16 = 40$! Wait: $15 + 9 + 16 = 40$, $\\sqrt{40} = 2\\sqrt{10}$. If we divide $2x^2 + 2y^2 - 12x + 16y - 22 = 0$ by 2: $x^2 + y^2 - 6x + 8y = 11$. Then $(x-3)^2 + (y+4)^2 = 11 + 9 + 16 = 36$. Radius is $\\sqrt{36} = 6$!"
        ),
        # Q26 SPR (Trigonometry: Altitude Hypotenuse Product)
        (
            DOMAINS["MATH"]["GEOM"], "Right Triangles", "Hard",
            "In right triangle $ABC$ with right angle at $C$, the lengths of sides $AC$ and $BC$ are 15 and 20, respectively. An altitude $CD$ is drawn from $C$ to hypotenuse $AB$. What is the length of altitude $CD$?",
            "Enter the exact integer value of altitude CD:",
            ["12"],
            "Hypotenuse $AB = \\sqrt{15^2 + 20^2} = \\sqrt{225 + 400} = \\sqrt{625} = 25$. Triangle area $= \\frac{1}{2} \\times AC \\times BC = \\frac{1}{2} \\times 15 \\times 20 = 150$. Also, area $= \\frac{1}{2} \\times AB \\times CD = \\frac{1}{2} \\times 25 \\times CD = 150 \\implies 12.5 \\times CD = 150 \\implies CD = 12$."
        ),
        # Q27 SPR (Advanced Algebra: Equivalent Rates)
        (
            DOMAINS["MATH"]["ALG"], "Rates and Work", "Hard",
            "Two industrial water inlet pipes, Pipe A and Pipe B, can together fill an empty reservoir in 6 hours when operating simultaneously. Pipe A alone takes 5 hours less than Pipe B alone to fill the reservoir. How many hours does it take Pipe A alone to fill the reservoir?",
            "Enter the exact integer number of hours:",
            ["10"],
            "Let $t$ be hours for Pipe A alone; then Pipe B takes $t + 5$ hours. Work equation: $\\frac{1}{t} + \\frac{1}{t + 5} = \\frac{1}{6}$. Multiply by $6t(t + 5)$: $6(t + 5) + 6t = t(t + 5) \\implies 12t + 30 = t^2 + 5t \\implies t^2 - 7t - 30 = 0$. Factor: $(t - 10)(t + 3) = 0$. Since time must be positive, $t = 10$ hours."
        )
    ]

    for m, spec in enumerate(math_m2_sprs):
        domain, subdomain, diff, stim, prompt, answers, expl = spec
        if m == 2: # Fix Q25 numbers
            stim = "A circle in the xy-plane has equation $2x^2 + 2y^2 - 12x + 16y - 22 = 0$. What is the radius of the circle?"
            answers = ["6"]
            expl = "Divide by 2: $x^2 + y^2 - 6x + 8y = 11$. Complete the square: $(x - 3)^2 + (y + 4)^2 = 11 + 9 + 16 = 36$. Radius is $\\sqrt{36} = 6$."
        math_m2.append(make_spr(f"t1-math-m2-q{m+23}", domain, subdomain, diff, stim, prompt, answers, expl))

    test1_data = {
        "id": "test-1",
        "title": "SAT Practice Test 1 (2026 Edition)",
        "description": "Full-length Digital SAT 2026 practice examination matching official College Board Bluebook specifications. Features rigorous multistage adaptive difficulty, sophisticated reading passages, complex multi-step math problems, and balanced answer distributions.",
        "totalQuestions": 108,
        "sections": {
            "rw": {
                "id": "rw",
                "title": "Reading and Writing",
                "timeMinutes": 64,
                "modules": [
                    {
                        "id": "test-1-rw-m1",
                        "moduleNumber": 1,
                        "title": "Reading and Writing - Module 1",
                        "timeLimitSeconds": 1920,
                        "questions": rw_m1
                    },
                    {
                        "id": "test-1-rw-m2",
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
                        "id": "test-1-math-m1",
                        "moduleNumber": 1,
                        "title": "Math - Module 1",
                        "timeLimitSeconds": 2100,
                        "questions": math_m1
                    },
                    {
                        "id": "test-1-math-m2",
                        "moduleNumber": 2,
                        "title": "Math - Module 2",
                        "timeLimitSeconds": 2100,
                        "questions": math_m2
                    }
                ]
            }
        }
    }

    output_path = os.path.join("src", "data", "test1.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("// Digital SAT 2026 Practice Test 1 (High-Difficulty Edition)\n")
        f.write("export const test1 = " + json.dumps(test1_data, indent=2) + ";\n")
    print(f"Test 1 successfully written to {output_path} with {len(rw_m1)+len(rw_m2)+len(math_m1)+len(math_m2)} questions.")

if __name__ == "__main__":
    build_test1()
