# gen_test1_part2.py - Test 1 RW Module 2 (27 questions)
import json
from generate_suite_all import DOMAINS, make_mcq, make_bullet_notes, make_dual_passage, make_table

rw2 = []

# 1-4 Advanced Words in Context
rw2.append(make_mcq(
    "t1-rw-m2-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Although the initial laboratory trials showed promising enzymatic breakdown of synthetic polymers, the chemical engineers cautioned that the reaction rate tends to _____ dramatically when ambient temperatures drop below fifteen degrees Celsius.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["attenuate", "proliferate", "culminate", "fluctuate"],
    "A",
    "Choice A is correct. 'Attenuate' means to weaken or reduce in force or intensity. The context indicates the enzymatic reaction slows down/weakens under lower temperatures."
))

rw2.append(make_mcq(
    "t1-rw-m2-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "In his concluding chapter, the political theorist does not merely _____ the arguments of previous scholars; rather, he synthesizes their disparate frameworks into a novel taxonomy of constitutional jurisprudence.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["recapitulate", "repudiate", "fabricate", "obviate"],
    "A",
    "Choice A is correct. 'Recapitulate' means to summarize or restate the main points. The sentence contrasts merely restating previous scholars' points with synthesizing them into a new taxonomy."
))

rw2.append(make_mcq(
    "t1-rw-m2-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The diplomatic envoy was celebrated for her exceptionally _____ demeanor, maintaining an impenetrable poker face during hostile treaty negotiations that unnerved opposing delegations.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["impassive", "effusive", "bellicose", "querulous"],
    "A",
    "Choice A is correct. 'Impassive' means emotionless or serene. Maintaining an impenetrable poker face during tense talks exemplifies an impassive demeanor."
))

rw2.append(make_mcq(
    "t1-rw-m2-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The restoration team discovered that previous 19th-century conservators had applied a heavy, varnish-based coating that had over time _____ the luminous, delicate tempera underlayers applied by the Florentine master.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["obscured", "explicated", "rejuvenated", "demarcated"],
    "A",
    "Choice A is correct. 'Obscured' means concealed or darkened. The heavy varnish covered up and hid the original delicate tempera paint."
))

# 5-8 Cross-Text Connections & Structure
rw2.append(make_mcq(
    "t1-rw-m2-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Anthropologist Samuel Vance contends that the decline of major urban centers in the Bronze Age Indus Valley was precipitated primarily by systemic trade route disruptions across the Persian Gulf, which impoverished craft guilds and undermined centralized municipal sanitation.",
        "Geoscientist Linda Chen analyzed oxygen isotope ratios in speleothems from regional caves and concluded that a multi-century weakening of the summer monsoon drastically reduced river discharges across the Indus basin, forcing agrarian populations to disperse east into smaller agricultural hamlets."
    ),
    "Based on the texts, how would Chen (Text 2) most likely characterize Vance's explanation in Text 1?",
    [
        "As attributing the urban collapse to socioeconomic factors while failing to account for regional hydroclimatic collapse.",
        "As overstating the resilience of rural agricultural hamlets during sustained continental droughts.",
        "As providing conclusive geological evidence that maritime trade routes flourished throughout the Bronze Age.",
        "As proving that municipal sanitation systems were unaffected by environmental fluctuations."
    ],
    "A",
    "Choice A is correct. Vance focuses exclusively on mercantile trade disruption, whereas Chen's geological speleothem data demonstrates that massive monsoon failure and water depletion caused the societal collapse."
))

rw2.append(make_mcq(
    "t1-rw-m2-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Emily Dickinson's poetic output is distinguished by unconventional capitalization, erratic dash punctuation, and idiosyncratic slant rhymes. While traditional 19th-century editors sanitized these features to conform to Victorian metrical regularities, contemporary literary scholars celebrate these syntactic disruptions as deliberate aesthetic choices designed to embody the fractured, hesitating nature of subjective human consciousness.",
    "Which choice best states the primary purpose of the text?",
    [
        "To contrast 19th-century editorial dismissals of Dickinson's style with modern appreciation of its expressive function.",
        "To argue that Dickinson deliberately modeled her punctuation on English liturgical hymns.",
        "To provide a chronological biography of Dickinson's publishing relationship with 19th-century editors.",
        "To criticize modern editors for failing to correct typographical errors in early print editions."
    ],
    "A",
    "Choice A is correct. The text contrasts how 19th-century editors smoothed over Dickinson's syntax with how modern scholars view her syntactic disruptions as deliberate aesthetic representations of consciousness."
))

rw2.append(make_mcq(
    "t1-rw-m2-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
    "Biochemist Dr. Kenji Sato cautions that while machine learning algorithms have revolutionized protein structure prediction, they cannot reliably predict allosteric conformational changes occurring upon ligand binding. <u>Because deep-learning models are trained on static crystallographic databases, they inherently underestimate the dynamic, entropy-driven thermodynamic landscapes that govern protein-substrate kinetics in living cytoplasm.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It provides a mechanistic explanation for the methodological limitation highlighted in the preceding sentence.",
        "It refutes the claim that protein folding can be modeled through machine learning algorithms.",
        "It proposes an experimental protocol to replace crystallographic imaging with dynamic thermodynamic sensors.",
        "It summarizes the historical development of machine learning in computational biochemistry."
    ],
    "A",
    "Choice A is correct. The first sentence highlights a limitation (algorithms cannot predict allosteric changes), and the underlined sentence explains why (training on static crystals underrepresents dynamic thermodynamic states)."
))

rw2.append(make_mcq(
    "t1-rw-m2-q8", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Ethicist Julian Rivera argues that algorithmic decision-making in medical diagnostics eliminates human diagnostic bias and should be made mandatory for preliminary radiology screening across all acute care hospitals.",
        "Physician Maya Lin cautions that diagnostic algorithms frequently replicate historical training disparities, misclassifying pathology in patient demographics that are underrepresented in baseline clinical imagery databases."
    ),
    "Based on the texts, how does Lin's perspective in Text 2 differ from Rivera's perspective in Text 1?",
    [
        "Lin identifies a source of systematic algorithmic error that contradicts Rivera's claim of bias-free diagnostic automation.",
        "Lin advocates for the complete elimination of radiology departments in modern acute care facilities.",
        "Lin demonstrates that human radiologists possess higher perceptual speed than any computer vision system.",
        "Lin argues that demographic disparities in medicine are caused solely by differences in insurance coverage."
    ],
    "A",
    "Choice A is correct. Rivera claims automated diagnostics eliminate human bias, but Lin shows algorithms encode and replicate training disparities, directly challenging Rivera's assertion."
))

# 9-14 Information and Ideas
table_q9 = make_table(
    ["Aerosol Type", "Mean Particle Size (nm)", "Optical Depth", "Radiative Forcing (W/m²)"],
    [
        ["Sulfate", "180", "0.28", "-0.45"],
        ["Black Carbon", "85", "0.08", "+0.35"],
        ["Sea Salt", "420", "0.19", "-0.22"],
        ["Mineral Dust", "650", "0.22", "-0.15"]
    ]
)
rw2.append(make_mcq(
    "t1-rw-m2-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Hard",
    table_q9 + "<br>Atmospheric scientists study the net climatic impact of airborne aerosols. Negative radiative forcing corresponds to a net cooling effect on global temperatures (reflecting solar radiation), whereas positive radiative forcing indicates net warming (absorbing infrared radiation).",
    "Which choice is best supported by the data in the table?",
    [
        "Sulfate aerosols produce the greatest net cooling effect of all four aerosol types evaluated.",
        "Black carbon produces a stronger cooling effect than sea salt particles.",
        "Mineral dust has the highest optical depth among the four aerosol categories.",
        "All four aerosol types exhibit positive radiative forcing."
    ],
    "A",
    "Choice A is correct. Sulfate aerosols have a radiative forcing of -0.45 W/m², which is the most negative value in the table, indicating the greatest net cooling effect."
))

rw2.append(make_mcq(
    "t1-rw-m2-q10", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "In her analysis of ancient Mesopotamian agriculture, archaeologist Dr. Fatima Al-Hassan argues that the transition from emmer wheat cultivation to barley in southern Sumerian city-states between 2400 BCE and 1800 BCE was an adaptive response to progressive soil salinization caused by intensive irrigation.",
    "Which archaeological finding, if true, would most directly support Al-Hassan's argument?",
    [
        "Laboratory grain testing showing that ancient barley varieties tolerated four times the soil salinity concentrations that caused emmer wheat crops to fail.",
        "Tablets indicating that the price of emmer wheat remained permanently higher than barley throughout Mesopotamia.",
        "Excavations showing that ceramic irrigation canals in Sumer were constructed from unbaked sun-dried clay.",
        "Pollen records demonstrating that date palm orchards expanded alongside emmer wheat fields during the same period."
    ],
    "A",
    "Choice A is correct. Showing that barley tolerated four times higher soil salinity than emmer directly corroborates the claim that switching to barley was a response to salinization."
))

rw2.append(make_mcq(
    "t1-rw-m2-q11", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Marine biologists studying bioluminescent dinoflagellates noted that these single-celled algae flash brilliant blue light upon mechanical deformation of their cell membranes, such as when water is disturbed by swimming predators. Researchers hypothesized that this luminescence serves as a 'burglar alarm,' exposing the swimming copepod predators to larger tertiary hunters such as fish. When researchers placed copepods and dinoflagellates in a dark tank containing juvenile fish, fish predation on copepods increased fivefold in turbulent water compared to still water. However, when dinoflagellates engineered to lack luciferase (the light-emitting enzyme) were used under identical turbulent conditions, fish predation rates did not increase above still-water baselines. This result strongly implies that _____.",
    "Which choice most logically completes the text?",
    [
        "the elevated predation on copepods was triggered by the visual bioluminescent flash rather than physical water turbulence alone",
        "dinoflagellates rely exclusively on chemical toxins rather than optical emissions to deter microscopic grazers",
        "copepods navigate dark aquatic environments by actively tracking the blue light pulses emitted by dinoflagellates",
        "juvenile fish locate copepod prey by detecting mechanical pressure waves rather than visual light cues"
    ],
    "A",
    "Choice A is correct. When luminescence was eliminated (luciferase-lacking mutants), the predation increase disappeared despite turbulence remaining constant, proving the light flash was the causal factor."
))

rw2.append(make_mcq(
    "t1-rw-m2-q12", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "For centuries, historians attributed the rapid collapse of the Norse settlements in southern Greenland during the 15th century solely to abrupt climatic cooling associated with the Little Ice Age. Recent bioarchaeological analyses of carbon and nitrogen isotopes in skeletal remains, however, complicate this mono-causal narrative. The isotopic signatures demonstrate that the Norse diet shifted dramatically over two centuries from 80 percent terrestrial livestock to more than 70 percent marine resources (specifically seals), proving that the colonists exhibited substantial adaptive resilience. The eventual abandonment was likely catalyzed by compound factors, including declining European ivory markets for walrus tusks, pirate raids, and soil erosion.",
    "Which choice best summarizes the central idea of the text?",
    [
        "Isotopic evidence reveals that the Greenland Norse adapted their diet to changing conditions, suggesting their abandonment resulted from multifaceted economic and environmental pressures rather than climate cooling alone.",
        "The Little Ice Age forced Greenland Norse settlers to abandon seal hunting and return to cattle husbandry prior to their extinction.",
        "European demand for walrus ivory was the sole factor preventing the Norse from developing sustainable maritime fishing techniques.",
        "Skeletal analysis proves that nutritional deficiencies resulting from a seal-based diet caused the demise of the Norse colony."
    ],
    "A",
    "Choice A is correct. The text shows dietary adaptation (shifting to marine seals) proved resilience, indicating collapse was due to complex combined factors rather than just climate cooling."
))

rw2.append(make_mcq(
    "t1-rw-m2-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "In behavioral economics, the 'endowment effect' describes the tendency of individuals to value an object more highly once they establish psychological ownership of it. In a classic experiment, participants randomly given a ceramic coffee mug demanded twice as much money to sell it as unendowed participants were willing to pay to purchase it. Neuroimaging reveals that contemplating the sale of an owned item activates the insula, an area of the brain associated with pain and disgust, whereas merely deciding whether to buy an item does not. This neurological pattern suggests that the endowment effect _____.",
    "Which choice most logically completes the text?",
    [
        "is driven fundamentally by an aversion to perceived loss rather than by an objective appreciation of an item's intrinsic utility",
        "disappears completely whenever monetary transactions are conducted through anonymous electronic exchanges",
        "occurs only among individuals who exhibit hyperactive cognitive processing in the prefrontal cortex",
        "causes consumers to systematically overvalue commodities that have low manufacturing costs"
    ],
    "A",
    "Choice A is correct. Activation of the insular cortex (linked to pain and loss) during sales demonstrates that the endowment effect is rooted in loss aversion rather than objective utility."
))

rw2.append(make_mcq(
    "t1-rw-m2-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "The mycorrhizal networks connecting temperate forest trees are often described colloquially as a harmonious 'wood-wide web.' However, forest ecologists point out that these fungal conduits are fundamentally transactional arenas driven by reciprocal exploitation. Trees that fail to supply surplus photosynthates to the fungi are selectively choked off from phosphorus and nitrogen supplies, and larger mature trees frequently utilize the network to export allelopathic biochemical inhibitors that suppress the germination of competing understory seedlings.",
    "According to the text, how do mature trees sometimes utilize mycorrhizal networks against competitors?",
    [
        "By transmitting chemical inhibitors through the fungal network to suppress the growth of neighboring seedlings.",
        "By absorbing all moisture from the canopy to cause localized drought conditions around saplings.",
        "By producing enzymes that break down fungal hyphae in the root systems of nearby competitors.",
        "By recruiting parasitic insect species to feed exclusively on the foliage of adjacent trees."
    ],
    "A",
    "Choice A is correct. The text explicitly states that mature trees 'frequently utilize the network to export allelopathic biochemical inhibitors that suppress the germination of competing understory seedlings'."
))

# 15-21 Standard English Conventions (Grammar)
rw2.append(make_mcq(
    "t1-rw-m2-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
    "The committee considered three distinct proposals: Dr. Aris's plan to expand public transit _____ Dr. Gomez's initiative to subsidize municipal rooftop solar arrays; and Director Vance's proposal to revitalize waterfront wetlands.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["corridors;", "corridors,", "corridors", "corridors—"],
    "A",
    "Choice A is correct. In a complex list where individual list items contain internal commas (or parallel semicolon separation is already established, as in '; and Director Vance...'), semicolons must separate the items."
))

rw2.append(make_mcq(
    "t1-rw-m2-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The lead researcher explained that the expedition's primary objective—locating the subterranean fossil chambers of the submerged karst _____ had been accomplished despite severe flooding.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["caves—", "caves,", "caves;", "caves"]
    ,"A",
    "Choice A is correct. A pair of em-dashes is required to set off the parenthetical appositive phrase ('—locating the subterranean fossil chambers of the submerged karst caves—')."
))

rw2.append(make_mcq(
    "t1-rw-m2-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "Neither the lead conservationist nor the field technicians _____ able to account for the sudden resurgence of the endangered ivory-billed woodpecker in the remote river basin.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["was", "were", "is", "has been"],
    "B",
    "Choice B is correct. In a 'neither... nor' construction, the verb agrees with the closer subject: 'field technicians' (plural), which takes 'were'."
))

rw2.append(make_mcq(
    "t1-rw-m2-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Hard",
    "Synthesized in the laboratory using high-pressure chemical vapor deposition, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the synthetic diamonds possessed an optical clarity exceeding that of naturally occurring stones.",
        "materials scientists praised the synthetic diamonds for having an optical clarity that exceeded natural stones.",
        "the optical clarity of the synthetic diamonds exceeded that of naturally occurring stones.",
        "it was found that the synthetic diamonds possessed higher optical clarity than natural stones."
    ],
    "A",
    "Choice A is correct. The introductory participial modifier 'Synthesized in the laboratory...' must logically describe 'the synthetic diamonds'."
))

rw2.append(make_mcq(
    "t1-rw-m2-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "Astronomers originally classified Pluto as the solar system's ninth planet; _____ the discovery of Eris and other massive trans-Neptunian objects in the Kuiper Belt prompted the International Astronomical Union to reclassify it as a dwarf planet in 2006.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["however,", "moreover,", "similarly,", "furthermore,"],
    "A",
    "Choice A is correct. 'However,' signals the contrast between the historical classification of Pluto as a planet and its subsequent demotion to dwarf planet."
))

rw2.append(make_mcq(
    "t1-rw-m2-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Each of the participating laboratories submitted _____ experimental protocols to the bioethics oversight panel prior to initiating clinical trials.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["its", "their", "they're", "it's"],
    "A",
    "Choice A is correct. 'Each' is grammatically singular and requires the singular possessive pronoun 'its'."
))

rw2.append(make_mcq(
    "t1-rw-m2-q21", DOMAINS["RW"]["CONV"], "Parallel Structure", "Medium",
    "The new urban planning ordinance aims to reduce vehicular emissions, promote public transit ridership, and _____ pedestrian accessibility across commercial corridors.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["expand", "expanding", "to expanding", "expands"],
    "A",
    "Choice A is correct. The parallel verb series consists of base verbs: 'reduce...', 'promote...', and 'expand...'."
))

# 22-24 Transitions
rw2.append(make_mcq(
    "t1-rw-m2-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "Geologists long believed that the Appalachian Mountains were formed in a single catastrophic tectonic collision. _____, modern paleogeographic mapping indicates that the range resulted from three distinct orogenic events occurring over a span of two hundred million years.",
    "Which choice completes the text with the most logical transition?",
    ["To the contrary,", "In addition,", "For example,", "Consequently,"],
    "A",
    "Choice A is correct. 'To the contrary,' introduces the modern finding that directly refutes the single-collision belief."
))

rw2.append(make_mcq(
    "t1-rw-m2-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "Traditional lithium-ion batteries utilize flammable liquid organic electrolytes that pose thermal runaway risks if punctured. _____, solid-state battery designs replace volatile liquids with ceramic or polymer electrolytes, substantially reducing combustion risks.",
    "Which choice completes the text with the most logical transition?",
    ["In response,", "Likewise,", "Specifically,", "Nevertheless,"],
    "A",
    "Choice A is correct. 'In response,' signals that solid-state batteries were developed directly to address and solve the liquid electrolyte safety hazard."
))

rw2.append(make_mcq(
    "t1-rw-m2-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "The author's prose is deceptively simple, employing commonplace diction and short declarative sentences. _____, this stylistic restraint generates an atmosphere of intense psychological claustrophobia.",
    "Which choice completes the text with the most logical transition?",
    ["Far from rendering the text flat,", "In other words,", "For instance,", "As a result,"],
    "A",
    "Choice A is correct. It smoothly transitions from the description of simple syntax to the surprising, impactful emotional intensity that this restraint produces."
))

# 25-27 Rhetorical Synthesis
rw2.append(make_mcq(
    "t1-rw-m2-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Zaha Hadid (1950–2016) was an Iraqi-British architect celebrated for her revolutionary parametric designs.",
        "Parametric architecture utilizes algorithmic computation to generate curvilinear, fluid structural geometries.",
        "In 2004, Hadid became the first woman to win the prestigious Pritzker Architecture Prize.",
        "One of her most celebrated works is the Heydar Aliyev Center in Baku, Azerbaijan, completed in 2012.",
        "The building features an undulating, continuous roofline with no sharp angles or visible columns."
    ]),
    "The student wants to highlight the unique architectural style of the Heydar Aliyev Center. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Designed by Zaha Hadid, the Heydar Aliyev Center exemplifies parametric architecture with an undulating, continuous roofline devoid of sharp angles or visible columns.",
        "In 2004, Zaha Hadid became the first woman to win the Pritzker Architecture Prize for her algorithmic building designs.",
        "Completed in 2012 in Baku, Azerbaijan, the Heydar Aliyev Center is one of the most famous buildings designed by an Iraqi-British architect.",
        "Parametric design allows contemporary architects to use computational algorithms to construct fluid, curvilinear geometries."
    ],
    "A",
    "Choice A is correct. It specifically highlights the unique architectural features of the Heydar Aliyev Center (undulating, continuous roofline with no sharp angles or columns)."
))

rw2.append(make_mcq(
    "t1-rw-m2-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Ancient Roman concrete (opus caementicium) has survived for millennia in marine environments.",
        "Modern Portland concrete typically degrades within decades when exposed to seawater.",
        "Roman concrete incorporated volcanic ash from the Pozzuoli region near Naples.",
        "When exposed to seawater, minerals in the volcanic ash react with lime to form aluminous tobermorite crystals.",
        "These interlocking tobermorite crystals reinforce microcracks, giving the concrete self-healing properties."
    ]),
    "The student wants to explain the chemical mechanism responsible for the longevity of Roman marine concrete. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "When exposed to seawater, volcanic ash in Roman concrete reacts with lime to crystallize into aluminous tobermorite, interlocking crystals that actively self-heal structural microcracks.",
        "Unlike modern Portland concrete, which deteriorates in decades, Roman concrete incorporated volcanic ash sourced near Naples.",
        "Roman concrete, known as opus caementicium, has endured for millennia in marine environments across the Mediterranean.",
        "Tobermorite crystals are minerals that form through chemical reactions between lime and volcanic materials."
    ],
    "A",
    "Choice A is correct. It provides the specific chemical mechanism: seawater reacting with volcanic ash and lime to form tobermorite crystals that self-heal cracks."
))

rw2.append(make_mcq(
    "t1-rw-m2-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "CRISPR-Cas9 gene editing traditionally creates double-stranded DNA breaks.",
        "Double-stranded breaks can occasionally trigger unintended insertions or deletions (indels).",
        "Base editing, developed by David Liu in 2016, uses a modified Cas9 nickase fused to a deaminase enzyme.",
        "Base editors chemically convert single nucleotide bases (e.g., C to T, or A to G) without cutting both DNA strands.",
        "This approach dramatically reduces indels while correcting point mutations associated with genetic diseases."
    ]),
    "The student wants to emphasize an advantage of base editing over traditional CRISPR-Cas9. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "By chemically converting single nucleotide bases without cutting both DNA strands, base editing minimizes unwanted indels compared to traditional CRISPR-Cas9.",
        "Developed in 2016 by David Liu, base editing relies on a Cas9 nickase fused to a deaminase enzyme.",
        "Traditional CRISPR-Cas9 introduces double-stranded DNA breaks that can introduce point mutations into host genomes.",
        "Both CRISPR-Cas9 and base editors are revolutionary biotechnology tools used to target genetic diseases."
    ],
    "A",
    "Choice A is correct. It explicitly highlights the advantage: avoiding double-stranded cuts and reducing unwanted indels."
))

print(f"Test 1 RW Module 2 ready: {len(rw2)} questions.")
