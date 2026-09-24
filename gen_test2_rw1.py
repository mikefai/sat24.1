# gen_test2.py - Practice Test 2 (108 questions)
import json
import os
from generate_suite_all import DOMAINS, make_mcq, make_spr, make_bullet_notes, make_dual_passage, make_table

rw1 = []
rw2 = []
math1 = []
math2 = []

# ==========================================
# TEST 2 - READING & WRITING MODULE 1 (27 Qs)
# ==========================================

# 1-4 Words in Context
rw1.append(make_mcq(
    "t2-rw-m1-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Easy",
    "Although the initial findings of the ornithological survey appeared _____, subsequent long-term telemetry data revealed that the population of yellow-breasted warblers was actually undergoing a severe, steady decline.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["auspicious", "negligible", "tentative", "erratic"],
    "A",
    "Choice A is correct. 'Auspicious' means promising, favorable, or indicating success. The contrast ('Although... auspicious, subsequent data revealed... a severe decline') establishes that the initial findings seemed positive."
))

rw1.append(make_mcq(
    "t2-rw-m1-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Unlike her predecessor, who often delivered dogmatic proclamations, Justice Morales was known for her _____ approach to legal interpretation, carefully weighing empirical statutory consequences rather than relying on abstract philosophical doctrines.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["pragmatic", "esoteric", "arbitrary", "impetuous"],
    "A",
    "Choice A is correct. 'Pragmatic' means guided by practical considerations and consequences rather than ideology or theoretical abstractions, directly contrasting with dogmatic."
))

rw1.append(make_mcq(
    "t2-rw-m1-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The museum curator noted that while digital reproduction technologies can democratize access to historic art, they cannot replicate the tactile _____ of aged impasto and micro-craquelure unique to the physical canvas.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["nuances", "distortions", "redundancies", "deficiencies"],
    "A",
    "Choice A is correct. 'Nuances' refers to subtle distinctions or details. Physical characteristics like impasto and micro-craquelure are tactile nuances that digital copies miss."
))

rw1.append(make_mcq(
    "t2-rw-m1-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The economist cautioned that the municipal government's short-term stimulus spending would merely _____ structural budget deficits rather than address the underlying stagnation in local manufacturing wages.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["palliate", "exacerbate", "adjudicate", "subvert"],
    "A",
    "Choice A is correct. 'Palliate' means to alleviate or mitigate symptoms temporarily without curing the underlying cause. Short-term spending palliates deficits rather than fixing wage stagnation."
))

# 5-8 Text Structure & Cross-Text Connections
rw1.append(make_mcq(
    "t2-rw-m1-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Paleontologist Dr. Simon Croft argues that the sudden extinction of Late Pleistocene megafauna across North America was caused almost exclusively by rapid climatic fluctuations during the Younger Dryas cooling event, which fragmented steppe habitats.",
        "Archaeologist Dr. Mara Jennings contends that while Younger Dryas climatic shifts placed physiological stress on megafauna, radiocarbon dating of butchery sites confirms that specialized human overkill was the indispensable factor that pushed giant ground sloths and mastodons to terminal extinction."
    ),
    "Based on the texts, how does Jennings (Text 2) view Croft's argument (Text 1)?",
    [
        "She views climate fluctuations as a contributing stressor but considers human hunting to be the decisive driving cause of extinction.",
        "She rejects the assertion that megafauna ever coexisted with prehistoric human hunters in North America.",
        "She contends that the Younger Dryas caused tropical forest expansion rather than steppe fragmentation.",
        "She agrees that human hunting had zero measurable impact on North American mastodon populations."
    ],
    "A",
    "Choice A is correct. Jennings acknowledges climatic stress ('while Younger Dryas shifts placed stress...'), but argues human overkill was the decisive factor, treating climate as only a partial factor."
))

rw1.append(make_mcq(
    "t2-rw-m1-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "In her 1813 novel <i>Pride and Prejudice</i>, Jane Austen utilizes free indirect discourse to blur the boundaries between the narrator's ironic commentary and Elizabeth Bennet's subjective internal reflections. <u>This narrative ambivalence forces the reader to actively scrutinize Elizabeth's hasty moral evaluations alongside the protagonist herself, transforming the reading experience into an exercise in deciphering cognitive prejudice.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It explains the psychological effect that Austen's narrative technique has on the reader.",
        "It summarizes the historical publishing reception of Jane Austen's early fiction.",
        "It provides evidence that Austen modeled Elizabeth Bennet on contemporary political figures.",
        "It criticizes the lack of moral clarity in 19th-century British domestic novels."
    ],
    "A",
    "Choice A is correct. The underlined sentence explicitly details how the narrative technique affects the reader ('forces the reader to actively scrutinize Elizabeth's hasty moral evaluations... transforming the reading experience')."
))

rw1.append(make_mcq(
    "t2-rw-m1-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Physicists studying quantum decoherence often encounter the boundary between quantum superposition and classical mechanics. While subatomic particles can exist in a superposition of multiple quantum states simultaneously, macroscopic objects in the everyday physical world never display such behavior. Environmental interactions—such as collisions with surrounding air molecules and photons—rapidly entangle the quantum system with its environment, destroying phase coherence and compelling the system to collapse into a single observable classical state.",
    "Which choice best describes the overall development of the passage?",
    [
        "A counterintuitive physical contrast is introduced, and a physical mechanism is described that accounts for that contrast.",
        "A longstanding scientific law is presented, followed by experimental evidence that completely invalidates it.",
        "Two competing laboratories are described along with their conflicting interpretations of quantum mechanics.",
        "The historical progression of Newtonian physics is traced from the 17th century through modern quantum theory."
    ],
    "A",
    "Choice A is correct. The text introduces the contrast between quantum superposition and macroscopic classical behavior, then explains the mechanism (environmental interaction destroying coherence)."
))

rw1.append(make_mcq(
    "t2-rw-m1-q8", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The botanical researchers discovered that the desert succulent's waxy cuticle is remarkably _____, preventing transpirational water loss even during the blistering peak heat of midday solar radiation.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["impermeable", "porous", "ephemeral", "malleable"],
    "A",
    "Choice A is correct. 'Impermeable' means not allowing fluid or moisture to pass through. A cuticle that prevents water loss during extreme heat is impermeable."
))

# 9-14 Information and Ideas
table_t2_q9 = make_table(
    ["Crop Variety", "Soil Salinity (dS/m)", "Germination Rate (%)", "Yield (% of normal)"],
    [
        ["Standard Wheat", "2.0", "94", "100"],
        ["Standard Wheat", "6.0", "42", "38"],
        ["Halophyte Hybrid A", "2.0", "92", "98"],
        ["Halophyte Hybrid A", "6.0", "88", "86"]
    ]
)
rw1.append(make_mcq(
    "t2-rw-m1-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Medium",
    table_t2_q9 + "<br>Agronomists are engineering salt-tolerant crop varieties to withstand irrigated soil salinization. They hypothesize that Halophyte Hybrid A maintains acceptable agricultural yields under elevated salinity stress where traditional wheat fails.",
    "Which choice best uses data from the table to support the agronomists' hypothesis?",
    [
        "At a salinity level of 6.0 dS/m, Halophyte Hybrid A retained an 86% yield and 88% germination rate, whereas Standard Wheat suffered severe reductions to 38% yield and 42% germination.",
        "Standard Wheat had a higher germination rate than Halophyte Hybrid A when cultivated under baseline soil conditions of 2.0 dS/m.",
        "Halophyte Hybrid A exhibited a slight decrease in yield when soil salinity increased from 2.0 dS/m to 6.0 dS/m.",
        "Both crop varieties demonstrated identical percentage drops in germination when exposed to high soil salinity."
    ],
    "A",
    "Choice A is correct. Comparing the performance of both crops at elevated salinity (6.0 dS/m) directly verifies that Hybrid A maintains high yield (86% vs 38%) and germination (88% vs 42%)."
))

rw1.append(make_mcq(
    "t2-rw-m1-q10", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Cognitive psychologists studying memory consolidation examined sleep-dependent synaptic plasticity. Mice trained on a spatial maze task were divided into two cohorts: Cohort 1 was allowed uninterrupted slow-wave sleep, while Cohort 2 was briefly awoken whenever electroencephalogram (EEG) recordings indicated delta-wave onset. Subsequent maze testing revealed that Cohort 1 navigated the maze with 85 percent accuracy, whereas Cohort 2 performed no better than naive control mice. Furthermore, neurochemical assay of hippocampal tissue in Cohort 1 showed elevated phosphorylation of synaptic scaffolding proteins required for long-term potentiation. These results strongly suggest that _____.",
    "Which choice most logically completes the text?",
    [
        "slow-wave delta sleep is essential for the molecular consolidation of spatial memories in mammalian hippocampal circuits",
        "spatial memory retention is driven entirely by visual cues processed during active daytime exploration",
        "waking mice during delta sleep permanently destroys their capacity to perform basic motor movements",
        "hippocampal scaffolding proteins are synthesized exclusively during rapid eye movement (REM) sleep"
    ],
    "A",
    "Choice A is correct. Disruption of slow-wave sleep prevented memory consolidation and blocked protein phosphorylation, demonstrating that slow-wave sleep is essential for spatial memory consolidation."
))

rw1.append(make_mcq(
    "t2-rw-m1-q11", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Easy",
    "In 1928, Alexander Fleming observed that a petri dish inoculated with <i>Staphylococcus</i> bacteria had become contaminated with blue-green mold, around which bacteria-free clear zones had formed. Rather than discarding the ruined culture, Fleming isolated the mold as <i>Penicillium notatum</i> and determined that it produced a soluble substance capable of lysing bacterial cell walls. Fleming's serendipitous observation and subsequent biochemical isolation revolutionized infectious disease treatment, inaugurating the modern era of antibiotic pharmacology.",
    "Which choice best summarizes the central idea of the text?",
    [
        "Fleming's accidental discovery and investigation of antibacterial mold secretions laid the foundation for antibiotic medicine.",
        "<i>Staphylococcus</i> bacteria are naturally immune to synthetic pharmacological compounds developed in clinical laboratories.",
        "Bacterial cultures in early 20th-century laboratories were frequently ruined by contamination from airborne fungal spores.",
        "Fleming spent decades intentionally synthesizing fungal enzymes to penetrate bacterial peptidoglycan layers."
    ],
    "A",
    "Choice A is correct. The text recounts Fleming's serendipitous observation of the bacterial lysis zone and his isolation of penicillin, which inaugurated antibiotic pharmacology."
))

rw1.append(make_mcq(
    "t2-rw-m1-q12", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "Historian Marcus Bailey argues that maritime navigation in the 15th-century Mediterranean relied heavily on portolan charts, not because they possessed accurate geometric latitude and longitude coordinates, but because they provided pragmatic, rhumb-line vector trajectories between coastal harbors.",
    "Which statement from a 15th-century mariner's journal would most directly support Bailey's argument?",
    [
        "\"We cared not for the celestial pole's degree, but steered steadily southwest along the chart's green rhumb line from Genoa straight toward Mallorca.\"",
        "\"The ship's chronometer was calibrated each morning at sunrise by the master astronomer.\"",
        "\"We refused to set sail until our mathematical astrolabe was polished and calibrated to three decimal places.\"",
        "\"The portolan parchment was useless for navigation because its scale was distorted by seawater stains.\""
    ],
    "A",
    "Choice A is correct. Setting aside celestial degrees and following rhumb-line vector lines directly supports Bailey's claim that navigators relied on practical rhumb lines rather than coordinates."
))

rw1.append(make_mcq(
    "t2-rw-m1-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Atmospheric scientists tracking methane emissions from subarctic permafrost thermokarst lakes discovered that ebullition (bubbling) releases far more gas than steady surface diffusion. During winter, when lake surfaces freeze solid, rising methane bubbles become trapped in layers of ice. If global temperatures continue to rise and shorten the annual ice cover duration, these trapped methane pockets will be released directly into the atmosphere earlier in the spring thaw. Because methane is a greenhouse gas with thirty times the warming potential of carbon dioxide, this accelerated release _____.",
    "Which choice most logically completes the text?",
    [
        "threatens to establish a positive feedback loop that amplifies ongoing Arctic warming trends",
        "will permanently eliminate all microbial anaerobic decomposition beneath thermokarst lakes",
        "is expected to cause widespread global atmospheric cooling during the winter months",
        "will convert subarctic lakes into sterile habitats incapable of sustaining aquatic life"
    ],
    "A",
    "Choice A is correct. Releasing a potent greenhouse gas earlier warms the climate further, which melts more permafrost and releases more methane, creating a positive feedback loop."
))

rw1.append(make_mcq(
    "t2-rw-m1-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "While conducting ethnobotanical fieldwork in Oaxaca, Mexico, researchers recorded indigenous culinary uses of wild chili peppers (<i>Capsicum annuum</i>). In addition to imparting pungent flavor, capsaicinoids in the peppers were traditionally valued for their antimicrobial properties in food preservation. Laboratory assays confirmed that crushed chilies suppressed the proliferation of common foodborne pathogens like <i>Salmonella</i> and <i>Listeria</i> by up to 90 percent in humid ambient storage.",
    "According to the text, what non-culinary benefit does capsaicinoid content provide?",
    [
        "It acts as a natural antimicrobial agent that inhibits foodborne bacterial pathogens.",
        "It enhances the vitamin C content of cured meats during winter refrigeration.",
        "It repels pollinating insects from agricultural spice plantations.",
        "It accelerates the fermentation of corn dough into alcoholic beverages."
    ],
    "A",
    "Choice A is correct. The text explicitly states that capsaicinoids were valued for antimicrobial food preservation and suppressed foodborne pathogens like Salmonella and Listeria."
))

# 15-21 Standard English Conventions
rw1.append(make_mcq(
    "t2-rw-m1-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "The restoration of the historic theater required months of painstaking _____ the decaying gilded moldings had to be reinforced by hand before modern acoustic baffling could be installed.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["labor: for example,", "labor; for instance,", "labor; because", "labor, because"],
    "D",
    "Choice D is correct. 'The restoration... labor' is an independent clause, followed by the dependent causal clause 'because the decaying gilded moldings had to be reinforced...'. A comma before because cleanly connects them."
))

rw1.append(make_mcq(
    "t2-rw-m1-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Easy",
    "Marine biologists have tracked migration routes of loggerhead sea _____ whose trans-Pacific journeys can span over eight thousand nautical miles.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["turtles,", "turtles;", "turtles:", "turtles"]
    ,"A",
    "Choice A is correct. A comma is required before the nonrestrictive relative clause 'whose trans-Pacific journeys can span over eight thousand nautical miles'."
))

rw1.append(make_mcq(
    "t2-rw-m1-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "The discovery of fossilized pollen grains alongside Neanderthal burial remains _____ that early hominins may have engaged in deliberate floral funerary practices.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["suggests", "suggest", "are suggesting", "have suggested"],
    "A",
    "Choice A is correct. The head subject is 'The discovery' (singular), requiring the singular verb 'suggests'. The prepositional phrase 'of fossilized pollen grains...' does not affect agreement."
))

rw1.append(make_mcq(
    "t2-rw-m1-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Medium",
    "Operating under extreme oceanic pressure and total darkness, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the autonomous robotic submersible mapped the hydrothermal vent field in high-resolution sonar.",
        "high-resolution sonar maps of the hydrothermal vent field were produced by the robotic submersible.",
        "it was possible for the robotic submersible to map the hydrothermal vent field.",
        "oceanographers monitored the robotic submersible as it mapped the hydrothermal vent field."
    ],
    "A",
    "Choice A is correct. The modifying participial phrase 'Operating under extreme oceanic pressure...' must logically modify 'the autonomous robotic submersible'."
))

rw1.append(make_mcq(
    "t2-rw-m1-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "In 1912, Alfred Wegener proposed the continental drift hypothesis; _____ lack of a plausible physical mechanism explaining how continents could plow through oceanic crust led most contemporary geologists to dismiss his ideas.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["however, his", "moreover, his", "for example, his", "in fact, his"],
    "A",
    "Choice A is correct. 'However, his' introduces the contrasting obstacle that caused contemporaries to reject Wegener's groundbreaking hypothesis."
))

rw1.append(make_mcq(
    "t2-rw-m1-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Although each of the participating choral ensembles performed _____ assigned madrigal flawlessly, the judges awarded the grand prize to the youth choir from Leipzig.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["its", "their", "they're", "it's"],
    "A",
    "Choice A is correct. 'Each' is grammatically singular and requires the singular possessive pronoun 'its'."
))

rw1.append(make_mcq(
    "t2-rw-m1-q21", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The astronomer's latest book investigates the origin of fast radio bursts—intense, millisecond-duration pulses of extragalactic radio _____ that continue to puzzle astrophysicists worldwide.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["waves—", "waves;", "waves,", "waves:"],
    "A",
    "Choice A is correct. An em-dash is needed to close the parenthetical descriptor that began with '—intense, millisecond-duration pulses of extragalactic radio waves—'."
))

# 22-24 Transitions
rw1.append(make_mcq(
    "t2-rw-m1-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Easy",
    "Standard concrete requires substantial quantities of freshwater during the curing process. _____, engineers in coastal regions have developed saltwater-tolerant cement mixtures that can cure using seawater, conserving scarce local aquifers.",
    "Which choice completes the text with the most logical transition?",
    ["In response,", "Meanwhile,", "Furthermore,", "Likewise,"],
    "A",
    "Choice A is correct. Developing saltwater-tolerant cement is a direct solution/response to the freshwater depletion issue mentioned in the first sentence."
))

rw1.append(make_mcq(
    "t2-rw-m1-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "The author's first novel was widely criticized for its melodramatic dialogue and predictable plotting. _____, her sophomore effort received universal acclaim, earning a nomination for the National Book Award.",
    "Which choice completes the text with the most logical transition?",
    ["In sharp contrast,", "Similarly,", "For instance,", "Consequently,"],
    "A",
    "Choice A is correct. 'In sharp contrast,' emphasizes the stark difference between the poor reception of the first book and the universal acclaim of the second."
))

rw1.append(make_mcq(
    "t2-rw-m1-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "Bumblebees maintain flight stability by flapping their wings at frequencies exceeding two hundred beats per second. _____, they generate miniature vortex airflows above their leading wing edges that produce rapid lift during hovering maneuvers.",
    "Which choice completes the text with the most logical transition?",
    ["In doing so,", "However,", "On the other hand,", "Nonetheless,"],
    "A",
    "Choice A is correct. 'In doing so,' logically explains how flapping their wings at high frequencies directly creates the vortex airflow that yields lift."
))

# 25-27 Rhetorical Synthesis
rw1.append(make_mcq(
    "t2-rw-m1-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "The Svalbard Global Seed Vault is located on the Norwegian island of Spitsbergen.",
        "It stores duplicate seed samples from gene banks around the world.",
        "The vault is buried 120 meters inside a sandstone mountain in the Arctic permafrost.",
        "Even if mechanical cooling fails, surrounding permafrost will keep the seeds frozen for decades.",
        "Its primary purpose is to safeguard global crop diversity against catastrophic loss."
    ]),
    "The student wants to explain how the vault's geographic location enhances its security. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Buried 120 meters inside an Arctic sandstone mountain, the Svalbard Global Seed Vault relies on natural permafrost to preserve seeds even in the event of mechanical cooling failure.",
        "Located on the Norwegian island of Spitsbergen, the Svalbard Global Seed Vault stores duplicate crop seeds from gene banks across the globe.",
        "The primary purpose of the Svalbard Global Seed Vault is to protect international crop diversity from environmental and agricultural crises.",
        "Natural permafrost allows Arctic facilities to maintain sub-zero temperatures without requiring constant electrical power."
    ],
    "A",
    "Choice A is correct. It directly addresses the prompt's goal: how the geographic setting (buried in sandstone permafrost) ensures security against mechanical failure."
))

rw1.append(make_mcq(
    "t2-rw-m1-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Hedy Lamarr was a celebrated Austrian-American Hollywood actress.",
        "During World War II, she collaborated with composer George Antheil to invent a radio guidance system for Allied torpedoes.",
        "Their system used frequency hopping to prevent enemy radio jamming.",
        "The transmitter and receiver synchronized frequency changes using miniature player-piano rolls.",
        "Frequency-hopping spread spectrum technology later became the foundational architecture for modern Wi-Fi and Bluetooth."
    ]),
    "The student wants to highlight the modern technological legacy of Lamarr and Antheil's wartime invention. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "The frequency-hopping radio guidance system co-invented by Hedy Lamarr during World War II later became the foundational architecture for modern Wi-Fi and Bluetooth technologies.",
        "During World War II, Hollywood actress Hedy Lamarr collaborated with composer George Antheil to develop an anti-jamming torpedo guidance system.",
        "Hedy Lamarr and George Antheil utilized synchronized miniature player-piano rolls to shift radio frequencies and avoid enemy interference.",
        "Frequency hopping is an electronic technique that prevents radio signal jamming by constantly changing communication channels."
    ],
    "A",
    "Choice A is correct. It explicitly highlights the modern legacy: frequency hopping becoming the foundation for Wi-Fi and Bluetooth."
))

rw1.append(make_mcq(
    "t2-rw-m1-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Tardigrades (water bears) are microscopic aquatic animals capable of entering a state of cryptobiosis.",
        "During cryptobiosis, metabolic activity drops to less than 0.01 percent of normal levels.",
        "Tardigrades synthesize unique intrinsically disordered proteins (TDPs) that vitrify into glass-like matrices to protect cellular structures.",
        "In this suspended state, tardigrades can survive extreme dehydration, cosmic radiation, and temperatures near absolute zero."
    ]),
    "The student wants to explain the molecular mechanism that enables tardigrades to survive cryptobiosis. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Tardigrades survive cryptobiosis by synthesizing intrinsically disordered proteins (TDPs) that vitrify into protective glass-like matrices around cellular structures.",
        "Entering cryptobiosis allows tardigrades to reduce their metabolic activity to less than 0.01 percent of baseline rates.",
        "Tardigrades are microscopic water bears that can survive extreme dehydration and temperatures near absolute zero.",
        "Cryptobiosis is a reversible state of suspended animation triggered by harsh environmental stressors."
    ],
    "A",
    "Choice A is correct. It specifies the precise molecular mechanism: synthesizing TDPs that vitrify into glass-like matrices to protect cellular structures."
))

print(f"Test 2 RW Module 1 ready: {len(rw1)} questions.")
