# gen_test4_rw1.py - Practice Test 4 RW Module 1 (27 questions)
import json
from generate_suite_all import DOMAINS, make_mcq, make_bullet_notes, make_dual_passage, make_table

rw1 = []

# 1-4 Words in Context
rw1.append(make_mcq(
    "t4-rw-m1-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Easy",
    "In her introductory remarks, the lead paleontologist emphasized that while the fossilized dinosaur footprint seemed _____, careful cast analysis revealed micro-striations proving that the theropod was sprinting rather than walking.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["ordinary", "fraudulent", "luminous", "indispensable"],
    "A",
    "Choice A is correct. 'Ordinary' means commonplace or unexceptional. The contrast ('while it seemed [ordinary], careful analysis revealed...') sets up the discovery of remarkable micro-striations."
))

rw1.append(make_mcq(
    "t4-rw-m1-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Although the CEO initially dismissed reports of software vulnerabilities as exaggerated rumors, subsequent penetration testing forced the executive to publicly _____ her previous denials and issue an urgent firmware patch.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["retract", "substantiate", "disseminate", "fabricate"],
    "A",
    "Choice A is correct. 'Retract' means to withdraw or take back a statement. After the vulnerability was proven, the CEO had to take back (retract) her earlier denials."
))

rw1.append(make_mcq(
    "t4-rw-m1-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The ethnomusicologist noted that the indigenous flute's melody possessed a haunting, _____ resonance that lingered in the acoustic chamber long after the musician had ceased breathing into the mouthpiece.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["ethereal", "cacophonous", "strident", "perfunctory"],
    "A",
    "Choice A is correct. 'Ethereal' means extremely delicate, light, or otherworldly. Describing a melody as a haunting resonance that lingers matches ethereal."
))

rw1.append(make_mcq(
    "t4-rw-m1-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "Unlike the talkative panelists who offered expansive commentaries on every agenda item, Dr. Vance was remarkably _____, speaking only when directly prompted by the moderator and offering brief, incisive observations.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["reticent", "garrulous", "effusive", "bellicose"],
    "A",
    "Choice A is correct. 'Reticent' means disposed to be silent or not speak freely; reserved. Speaking only when prompted and offering brief comments directly defines reticent."
))

# 5-8 Cross-Text Connections & Structure
rw1.append(make_mcq(
    "t4-rw-m1-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Cognitive psychologist Dr. Julian Ross contends that turn-by-turn satellite GPS navigation tools actively impair human spatial memory, citing neuroimaging studies showing reduced hippocampal gray matter volume in drivers who rely exclusively on automated digital mapping.",
        "Cartographic researcher Dr. Elena Gomez counters that digital navigation systems actually democratize spatial exploration, allowing individuals to navigate unfamiliar metropolitan environments with reduced cognitive anxiety, which enables them to focus attention on local architectural and cultural landmarks."
    ),
    "Based on the texts, how does Gomez (Text 2) view the impact of digital navigation described by Ross (Text 1)?",
    [
        "She focuses on how digital navigation reduces navigation anxiety and frees cognitive resources for cultural engagement, contrasting with Ross's emphasis on spatial memory impairment.",
        "She agrees that satellite navigation should be banned for drivers under the age of twenty-five.",
        "She proves that drivers who use paper road atlases experience higher rates of vehicular collisions.",
        "She disputes the neuroimaging findings showing that the human hippocampus is involved in spatial processing."
    ],
    "A",
    "Choice A is correct. Gomez highlights the psychological and cultural benefits (reducing anxiety, freeing attention for landmarks), directly presenting a constructive contrast to Ross's neurobiological concern."
))

rw1.append(make_mcq(
    "t4-rw-m1-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Mary Shelley's 1818 novel <i>Frankenstein</i> is structured as a complex epistolary frame narrative. The outer frame consists of Captain Robert Walton's letters to his sister, which encase Victor Frankenstein's harrowing oral narrative, which in turn encloses the Creature's central autobiographical confession. <u>This nested tripartite structure destabilizes moral certainty, forcing the reader to weigh Victor's accusations of monstrous malice against the Creature's poignant account of abandonment and societal cruelty.</u>",
    "Which choice best describes the function of the underlined sentence in the text as a whole?",
    [
        "It analyzes how the nested narrative structure prevents simplistic moral judgments about the characters.",
        "It summarizes the chronological sequence of Captain Walton's Arctic maritime expedition.",
        "It provides biographical context regarding Mary Shelley's relationship with Percy Bysshe Shelley.",
        "It criticizes early 19th-century British readers for misunderstanding the Creature's motives."
    ],
    "A",
    "Choice A is correct. The underlined sentence explicitly explains how the three-tier narrative structure destabilizes moral certainty and forces readers to evaluate conflicting perspectives."
))

rw1.append(make_mcq(
    "t4-rw-m1-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "In materials science, biomimicry involves emulating nature's time-tested patterns and structural strategies. For instance, the hydrophobic surface of the lotus leaf—covered with microscopic wax crystals that prevent water droplets from adhering—has inspired self-cleaning exterior architectural glass and paints. Similarly, the drag-reducing denticles found on shark skin have been replicated in high-performance hydrodynamic hulls and aircraft surfaces, demonstrating how millions of years of evolutionary optimization can resolve modern engineering bottlenecks.",
    "Which choice best states the primary purpose of the text?",
    [
        "To illustrate how biological adaptations inspire innovative engineering solutions in materials science.",
        "To argue that synthetic materials are inherently superior to naturally occurring biological polymers.",
        "To trace the historical origins of marine biology from the Renaissance through modern nanotechnology.",
        "To explain the chemical formulation of industrial waterproofing sealants."
    ],
    "A",
    "Choice A is correct. The passage introduces biomimicry and provides concrete examples (lotus leaves for self-cleaning paint, shark skin for drag reduction) to show how nature inspires modern engineering."
))

rw1.append(make_mcq(
    "t4-rw-m1-q8", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The municipal government's new sustainability initiative was remarkably _____, addressing transit emissions, renewable electrical generation, and municipal composting within a single unified policy framework.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["comprehensive", "cursory", "esoteric", "equivocal"],
    "A",
    "Choice A is correct. 'Comprehensive' means complete, thorough, or including all or nearly all elements. Combining transit, energy, and composting into one framework demonstrates comprehensive policy."
))

# 9-14 Information and Ideas
table_t4_q9 = make_table(
    ["Sub-basin", "Mean Depth (m)", "Dissolved Oxygen (μmol/kg)", "Fish Species Richness"],
    [
        ["Basin Alpha", "45", "210", "42"],
        ["Basin Beta", "85", "185", "38"],
        ["Basin Gamma", "140", "95", "16"],
        ["Basin Delta (Hypoxic)", "210", "32", "4"]
    ]
)
rw1.append(make_mcq(
    "t4-rw-m1-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Medium",
    table_t4_q9 + "<br>Marine ecologists hypothesize that species richness in coastal estuaries declines sharply when dissolved oxygen falls below 100 μmol/kg, with severe hypoxia (under 50 μmol/kg) resulting in near-total ecological collapse.",
    "Which choice best uses data from the table to support the ecologists' hypothesis?",
    [
        "Basin Gamma, with oxygen at 95 μmol/kg, had its species richness drop to 16, and Basin Delta (32 μmol/kg) plummeted to only 4 species, whereas Basins Alpha and Beta (above 180 μmol/kg) supported 38 to 42 species.",
        "Basin Alpha had greater water depth than Basin Beta, resulting in higher dissolved oxygen.",
        "Basin Gamma supported more fish species than Basin Delta because its water was significantly warmer.",
        "All four sub-basins exhibited identical dissolved oxygen levels during seasonal tidal cycles."
    ],
    "A",
    "Choice A is correct. It precisely checks both thresholds: oxygen dropping below 100 cut richness from 38-42 down to 16, and severe hypoxia (<50 in Delta) plummeted richness to just 4."
))

rw1.append(make_mcq(
    "t4-rw-m1-q10", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Biologists studying animal navigation examined magnetoreception in homing pigeons. Pigeons fitted with small brass bars (which do not disrupt magnetic fields) successfully navigated back to their lofts on both sunny and completely overcast days. However, pigeons fitted with miniature neodymium magnets flew off-course on overcast days, while navigating flawlessly on sunny days. This experimental outcome demonstrates that _____.",
    "Which choice most logically completes the text?",
    [
        "homing pigeons possess redundant navigational mechanisms, relying on geomagnetic cues primarily when solar compass cues are unavailable",
        "magnetic fields are the sole sensory mechanism utilized by birds for long-distance migratory orientation",
        "brass bars permanently deactivate retinal cryptochrome photoreceptors in avian eyes",
        "overcast skies prevent pigeons from detecting airborne auditory infrasound waves"
    ],
    "A",
    "Choice A is correct. Magnets only disrupted navigation when the sun was hidden (overcast), proving that pigeons use solar cues when available and only fall back on geomagnetic cues when the sun is blocked."
))

rw1.append(make_mcq(
    "t4-rw-m1-q11", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Easy",
    "The Rosetta Stone, carved in 196 BCE and rediscovered by French soldiers in 1799, proved to be the master key to deciphering ancient Egyptian hieroglyphs. The stela records an imperial decree issued at Memphis on behalf of King Ptolemy V, inscribed in three distinct scripts: Ancient Egyptian hieroglyphs (the sacred script of priests), Demotic (the cursive script of daily administration), and Ancient Greek (the language of the ruling court). Because scholars could readily read Ancient Greek, linguist Jean-François Champollion was able to cross-reference royal cartouches and decode the phonetic values of the hieroglyphs.",
    "Which choice best summarizes the central idea of the text?",
    [
        "The trilingual inscription on the Rosetta Stone provided the linguistic bridge that allowed scholars to decipher Egyptian hieroglyphs.",
        "Ptolemy V commissioned the Rosetta Stone to convert the Egyptian population to the Greek language.",
        "Hieroglyphs were strictly pictographic symbols with no underlying phonetic or alphabetic correspondence.",
        "French soldiers carved the Greek translation onto the Rosetta Stone following its 1799 excavation."
    ],
    "A",
    "Choice A is correct. The text explains that having the same decree in three scripts (including known Ancient Greek) enabled Champollion to decode the phonetic values of Egyptian hieroglyphs."
))

rw1.append(make_mcq(
    "t4-rw-m1-q12", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "In her study of early 20th-century aviation, historian Claire Bennett argues that the public celebration of early aviators was driven by a cultural desire to revive mythic ideals of individual heroic agency amidst an increasingly mechanized, bureaucratic industrial society.",
    "Which excerpt from a 1927 newspaper editorial would most directly support Bennett's argument?",
    [
        "\"In an age where human life is swallowed by assembly line gears and corporate ledgers, this solitary pilot soaring across the Atlantic proves that the indomitable individual spirit still conquers destiny.\"",
        "\"The airplane's radial engine consumed thirty-two gallons of aviation gasoline per hour of trans-oceanic flight.\"",
        "\"Municipal bonds have been approved to expand the municipal landing strip by twelve hundred feet.\"",
        "\"Commercial air travel ticket prices have declined seven percent across domestic eastern routes.\""
    ],
    "A",
    "Choice A is correct. Directly contrasting solitary pilot agency against corporate ledgers and assembly line gears supports Bennett's heroic individual agency thesis."
))

rw1.append(make_mcq(
    "t4-rw-m1-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "In physiological immunology, the hygiene hypothesis suggests that early childhood exposure to diverse microbes trains the immune system to distinguish between harmful pathogens and harmless antigens. In a longitudinal cohort study of 2,000 children raised either in industrialized cities or on traditional multi-species livestock farms, researchers tracked allergic asthma diagnoses through age twelve. Farm-raised children exhibited asthma rates 70 percent lower than urban peers. Intriguingly, blood samples from farm children revealed elevated baseline levels of regulatory T-cells (Tregs) that suppress inflammatory responses. This physiological pattern implies that _____.",
    "Which choice most logically completes the text?",
    [
        "microbial diversity in rural farm environments stimulates regulatory T-cell development that dampens inappropriate allergic hypersensitivity",
        "urban environments completely lack airborne dust particles and household allergens",
        "regulatory T-cells are synthesized exclusively in response to bacterial pneumonia infections",
        "industrialized city dwellers possess stronger genetic resistance to chronic inflammatory disorders"
    ],
    "A",
    "Choice A is correct. Farm-raised children had 70% lower asthma and elevated Tregs (which suppress inflammation), implying diverse farm microbes stimulate Tregs to prevent allergic hypersensitivity."
))

rw1.append(make_mcq(
    "t4-rw-m1-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "In astrophysics, pulsars are highly magnetized, rapidly rotating neutron stars that emit focused beams of electromagnetic radiation from their magnetic poles. Because a pulsar's magnetic axis is typically misaligned with its rotational axis, these emission beams sweep through space like a lighthouse beacon. When Earth lies along the beam's sweep path, radio telescopes detect pulses of extraordinary temporal precision, rivaling the accuracy of atomic clocks.",
    "According to the text, what causes the lighthouse-like periodic pulsing observed from pulsars?",
    [
        "The misalignment between the pulsar's magnetic emission axis and its rotational axis.",
        "Periodic thermonuclear detonations occurring on the neutron star's iron crust.",
        "Gravitational lensing caused by neighboring supermassive black holes.",
        "The rhythmic expansion and contraction of the pulsar's gaseous outer atmosphere."
    ],
    "A",
    "Choice A is correct. The text explicitly states that 'Because a pulsar's magnetic axis is typically misaligned with its rotational axis, these emission beams sweep through space like a lighthouse beacon'."
))

# 15-21 Standard English Conventions
rw1.append(make_mcq(
    "t4-rw-m1-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "The restoration of the Gothic cathedral's stained glass windows took nearly four _____ each individual pane of leaded glass had to be soaked in an ultrasonic cleansing bath before being re-soldered.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["years: because", "years; because", "years, because", "years because"],
    "C",
    "Choice C is correct. 'The restoration... took nearly four years' is an independent clause, followed by the dependent causal clause 'because each individual pane... had to be soaked...'. A comma before because cleanly and appropriately connects them."
))

rw1.append(make_mcq(
    "t4-rw-m1-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Easy",
    "Marine biologists captured high-definition footage of giant pacific _____ which can expand their arms to a span exceeding twenty feet.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["octopuses,", "octopuses;", "octopuses:", "octopuses"]
    ,"A",
    "Choice A is correct. A comma is required before the nonrestrictive relative clause 'which can expand their arms to a span exceeding twenty feet'."
))

rw1.append(make_mcq(
    "t4-rw-m1-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "The synthesis of carbon nanotubes from aerosolized ethylene gas _____ significant technical expertise and rigorous temperature regulation.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["requires", "require", "have required", "are requiring"],
    "A",
    "Choice A is correct. The singular head subject is 'The synthesis', which requires the singular verb 'requires'."
))

rw1.append(make_mcq(
    "t4-rw-m1-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Medium",
    "Trained to detect minute traces of explosive compounds, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the airport security canine alerted its handler to an unattended piece of luggage.",
        "the handler was alerted to an unattended piece of luggage by the security canine.",
        "an unattended piece of luggage was identified by the airport security canine.",
        "it was clear to the handler that the security canine had detected explosive residue."
    ],
    "A",
    "Choice A is correct. The introductory modifier 'Trained to detect minute traces of explosive compounds...' must logically modify 'the airport security canine'."
))

rw1.append(make_mcq(
    "t4-rw-m1-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "In 1859, Edwin Drake struck petroleum in Titusville, Pennsylvania; _____ the commercial viability of kerosene for indoor lighting fueled an unprecedented global oil boom.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["consequently,", "however,", "nevertheless,", "in contrast,"],
    "A",
    "Choice A is correct. 'Consequently,' establishes the cause-and-effect link between striking petroleum/proving kerosene viability and the resulting global oil boom."
))

rw1.append(make_mcq(
    "t4-rw-m1-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Before any pharmaceutical company can launch a nationwide vaccine campaign, _____ must submit phase-three clinical trial results to federal regulatory agencies.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["it", "they", "we", "he"],
    "A",
    "Choice A is correct. 'Pharmaceutical company' is an entity and grammatically singular, requiring the pronoun 'it'."
))

rw1.append(make_mcq(
    "t4-rw-m1-q21", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The chief aerodynamicist noted that the race car's rear wing—a complex airfoil crafted from autoclaved carbon _____ had provided thirty percent more downforce during high-speed cornering.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["fiber—", "fiber,", "fiber;", "fiber"]
    ,"A",
    "Choice A is correct. An em-dash is required to close the parenthetical descriptor that opened with '—a complex airfoil crafted from autoclaved carbon fiber—'."
))

# 22-24 Transitions
rw1.append(make_mcq(
    "t4-rw-m1-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Easy",
    "Excessive nitrogen runoff into freshwater lakes can trigger rapid algal blooms that deplete dissolved oxygen upon decomposing. _____, environmental agencies have established buffer strips of native vegetation along agricultural drainage canals to absorb fertilizer runoff.",
    "Which choice completes the text with the most logical transition?",
    ["To mitigate this ecological threat,", "In other words,", "By contrast,", "Nevertheless,"],
    "A",
    "Choice A is correct. Establishing native buffer strips is an action taken specifically to mitigate the algal bloom runoff threat."
))

rw1.append(make_mcq(
    "t4-rw-m1-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "The initial laboratory trials suggested that the experimental alloy would corrode under simulated marine conditions. _____, when tested in actual deep-sea benthic environments for twelve months, the alloy formed a protective passivation layer that completely prevented oxidative pitting.",
    "Which choice completes the text with the most logical transition?",
    ["Surprisingly,", "Consequently,", "Similarly,", "For instance,"],
    "A",
    "Choice A is correct. 'Surprisingly,' captures the unexpected positive outcome (passivation layer preventing corrosion) that contradicted the negative laboratory expectations."
))

rw1.append(make_mcq(
    "t4-rw-m1-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "Termites build towering subterranean mounds that maintain a constant internal temperature of 30°C despite external desert fluctuations. _____, they achieve this climate control entirely through passive convective ventilation shafts without consuming mechanical energy.",
    "Which choice completes the text with the most logical transition?",
    ["Remarkably,", "However,", "On the contrary,", "Instead,"],
    "A",
    "Choice A is correct. 'Remarkably,' emphasizes the impressive biological feat of achieving precise thermal control purely through passive structural ventilation."
))

# 25-27 Rhetorical Synthesis
rw1.append(make_mcq(
    "t4-rw-m1-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Rosalind Franklin was an English chemist and X-ray crystallographer.",
        "In 1952, Franklin and graduate student Raymond Gosling captured 'Photo 51'.",
        "Photo 51 is an X-ray diffraction image of crystallized B-form DNA fibers.",
        "The clear 'X' diffraction pattern provided decisive mathematical proof of DNA's helical structure.",
        "James Watson and Francis Crick utilized Franklin's unpublished data to build their double-helix model in 1953."
    ]),
    "The student wants to highlight the scientific significance of 'Photo 51'. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Captured in 1952 by Rosalind Franklin, 'Photo 51' produced an X-ray diffraction pattern that provided critical mathematical proof that DNA possesses a helical structure.",
        "Rosalind Franklin was an English chemist and X-ray crystallographer who conducted research in London during the early 1950s.",
        "In 1953, James Watson and Francis Crick constructed their celebrated molecular model of the double-helix.",
        "X-ray diffraction is an imaging technique that utilizes crystallized molecular fibers to examine sub-microscopic structures."
    ],
    "A",
    "Choice A is correct. It directly addresses the goal by highlighting the scientific importance of Photo 51 (providing decisive mathematical proof of DNA's helical geometry)."
))

rw1.append(make_mcq(
    "t4-rw-m1-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "CRISPR-Cas12 is an RNA-guided endonuclease enzyme used in molecular diagnostics.",
        "Unlike Cas9, Cas12 exhibits non-specific 'collateral cleavage' activity upon binding its specific target sequence.",
        "In diagnostic platforms like DETECTR, fluorescent reporter molecules are added to the sample.",
        "When Cas12 finds viral DNA, its collateral cleavage chops the reporter molecules, releasing a bright fluorescent glow.",
        "This allows rapid visual confirmation of viral infection in under thirty minutes without PCR thermocycling."
    ]),
    "The student wants to explain how Cas12's collateral cleavage is utilized to detect viral infections. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "In platforms like DETECTR, Cas12's collateral cleavage activates upon target binding to chop fluorescent reporter molecules, generating a glowing signal that confirms viral infection in under thirty minutes.",
        "CRISPR-Cas12 is an RNA-guided endonuclease that differs fundamentally from Cas9 in its catalytic behavior.",
        "Traditional PCR tests require expensive thermocycling machinery to amplify target viral genetic material.",
        "Diagnostic platforms rely on molecular endonucleases to bind specific genetic sequences in clinical samples."
    ],
    "A",
    "Choice A is correct. It directly explains how collateral cleavage detects viral infection: Cas12 binds viral DNA and chops fluorescent reporter molecules to produce a glowing signal."
))

rw1.append(make_mcq(
    "t4-rw-m1-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "New Zealand's Taupo Volcanic Zone possesses extensive subterranean geothermal reservoirs.",
        "The Wairakei geothermal power station opened in 1958, becoming the world's second commercial geothermal plant.",
        "Wairakei utilizes flash steam turbines that depressurize high-temperature subterranean brine.",
        "Today, geothermal energy generates approximately 18 percent of New Zealand's total national electricity.",
        "Geothermal power provides continuous baseload electricity that is unaffected by weather or seasonal droughts."
    ]),
    "The student wants to emphasize an operational advantage of geothermal energy over weather-dependent renewables. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Unlike weather-dependent renewables, geothermal power provides continuous baseload electricity that operates reliably regardless of weather conditions or seasonal droughts.",
        "Opened in 1958 in New Zealand's Taupo Volcanic Zone, the Wairakei geothermal station was the world's second commercial geothermal facility.",
        "Geothermal power plants like Wairakei generate approximately 18 percent of New Zealand's total electrical output.",
        "Flash steam turbines generate electrical energy by depressurizing high-temperature subterranean volcanic brine."
    ],
    "A",
    "Choice A is correct. It directly fulfills the goal by highlighting the operational advantage over weather-dependent renewables: providing continuous baseload power unaffected by weather or droughts."
))

print(f"Test 4 RW Module 1 ready: {len(rw1)} questions.")
