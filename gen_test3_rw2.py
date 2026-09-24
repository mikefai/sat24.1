# gen_test3_rw2.py - Practice Test 3 RW Module 2 (27 questions)
import json
from generate_suite_all import DOMAINS, make_mcq, make_bullet_notes, make_dual_passage, make_table

rw2 = []

# 1-4 Advanced Words in Context
rw2.append(make_mcq(
    "t3-rw-m2-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Although the documentary filmmaker claimed to present an objective retrospective of the trade summit, critics noted that her editing choices were distinctly _____, giving disproportionate airtime to anti-globalization activists while omitting the responses of international trade ministers.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["partisan", "scrupulous", "dispassionate", "inconsequential"],
    "A",
    "Choice A is correct. 'Partisan' means prejudiced in favor of a particular cause or side. Giving biased airtime to one side while excluding the other illustrates a partisan approach."
))

rw2.append(make_mcq(
    "t3-rw-m2-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The literary scholar warned against applying modern ethical frameworks to ancient epic poetry, arguing that evaluating Homeric warfare through contemporary human rights conventions is inherently _____ and distorts the cultural values of the Bronze Age Aegean.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["anachronistic", "subversive", "pedantic", "redundant"],
    "A",
    "Choice A is correct. 'Anachronistic' means belonging or appropriate to an earlier period, or placing a modern concept inappropriately into a historical past. Applying modern human rights to ancient Homeric poetry is anachronistic."
))

rw2.append(make_mcq(
    "t3-rw-m2-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The engineering board issued a scathing report condemning the bridge contractor's _____ inspection protocols, noting that technicians had merely glanced at rusted suspension cables without conducting ultrasonic ultrasonic stress testing.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["perfunctory", "rigorous", "exhaustive", "disinterested"],
    "A",
    "Choice A is correct. 'Perfunctory' means carried out with a minimum of effort or reflection. Merely glancing at rusted cables without real ultrasonic testing is perfunctory."
))

rw2.append(make_mcq(
    "t3-rw-m2-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "Far from being an intractable opponent of technological modernization, the museum director was remarkably _____, eagerly integrating augmented-reality tours into the classical antiquities wing.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["receptive", "indifferent", "bellicose", "dogmatic"],
    "A",
    "Choice A is correct. 'Receptive' means willing to consider or accept new suggestions and ideas. Eagerly integrating AR tours into ancient exhibits shows the director was receptive to technology."
))

# 5-8 Cross-Text Connections & Structure
rw2.append(make_mcq(
    "t3-rw-m2-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Urban planner Le Corbusier envisioned the 'Radiant City' as a triumph of rational modernism: vast, standardized skyscrapers surrounded by wide superhighways and green manicured parklands, organized through rigorous functional zoning that segregated industrial, commercial, and residential activities.",
        "Urban activist Jane Jacobs fiercely countered that high-density, mixed-use neighborhoods with short blocks, active sidewalks, and street-level storefronts are the true lifeblood of urban safety and economic vitality. She argued that Corbusier's sterile superblock towers dismantled the informal social networks that make cities livable."
    ),
    "Based on the texts, how would Jacobs (Text 2) most likely criticize Le Corbusier's Radiant City model (Text 1)?",
    [
        "By arguing that rigid functional zoning and isolated towers destroy the spontaneous, street-level community interactions essential to vibrant neighborhoods.",
        "By demonstrating that automobile superhighways are significantly less expensive to construct than traditional pedestrian walkways.",
        "By asserting that suburban sprawl provides a superior environment for commercial retail development.",
        "By agreeing that industrial factories should be situated directly adjacent to elementary schools."
    ],
    "A",
    "Choice A is correct. Jacobs directly opposes sterile superblocks and functional segregation, arguing that mixed-use, active sidewalks and short blocks create vibrant, livable cities."
))

rw2.append(make_mcq(
    "t3-rw-m2-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Gabriel García Márquez's 1967 masterpiece <i>One Hundred Years of Solitude</i> is celebrated for its mastery of magical realism, a mode that incorporates miraculous phenomena into realistic fiction without narrative astonishment. <u>When character Remedios the Beauty floats bodily up into the heavens while folding bed linens, the townspeople react not with horror or scientific skepticism, but merely lament the loss of their freshly ironed sheets.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It provides a vivid literary example that illustrates how the novel treats the supernatural as mundane reality.",
        "It summarizes the central political plot conflict running throughout García Márquez's narrative.",
        "It criticizes the lack of scientific realism in 20th-century Latin American fiction.",
        "It provides biographical context about García Márquez's childhood in rural Colombia."
    ],
    "A",
    "Choice A is correct. Remedios floating into heaven being treated as an inconvenience over sheets directly exemplifies how magical realism integrates miraculous events into ordinary life without astonishment."
))

rw2.append(make_mcq(
    "t3-rw-m2-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
    "In quantum physics, Bell's theorem mathematically proved that no physical theory based on 'local hidden variables' can ever reproduce all the statistical predictions of quantum mechanics. <u>Either the universe is non-local—meaning that measurements on one entangled particle instantaneously correlate with another regardless of distance—or counterfactual definiteness must be abandoned, meaning particles do not possess predetermined values prior to observation.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It presents the fundamental philosophical and physical implications resulting from Bell's theorem.",
        "It outlines an experimental apparatus used by Einstein to dispute quantum non-locality.",
        "It proves that light travels infinitely faster in a vacuum than previously calculated.",
        "It refutes the mathematical formulation of quantum mechanics derived by Erwin Schrödinger."
    ],
    "A",
    "Choice A is correct. The underlined sentence articulates the two profound ontological implications of Bell's theorem: non-locality or the abandonment of predetermined values."
))

rw2.append(make_mcq(
    "t3-rw-m2-q8", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Economist Dr. Keith Warren contends that universal basic income (UBI) unconditionally provided to all citizens eliminates extreme poverty while simultaneously stimulating consumer spending in local economies without administrative bloat.",
        "Labor economist Dr. Fiona Chen argues that unconditional cash transfers risk eroding workforce participation in essential entry-level industries, advocating instead for targeted wage subsidies (such as expansion of the Earned Income Tax Credit) that tie income supplements directly to employment."
    ),
    "Based on the texts, in what way do Warren and Chen primarily differ?",
    [
        "Warren supports unconditional income provision regardless of employment status, whereas Chen believes financial aid should be contingent upon workforce participation.",
        "Warren argues that poverty should be addressed solely through private philanthropy rather than state intervention.",
        "Chen claims that universal basic income increases employment rates in rural manufacturing communities.",
        "Both economists agree that entry-level wage subsidies cause macroeconomic stagnation."
    ],
    "A",
    "Choice A is correct. Warren champions unconditional income for all, while Chen advocates for targeted subsidies tied directly to employment."
))

# 9-14 Information and Ideas
table_t3_q9 = make_table(
    ["Benthic Trench", "Depth (m)", "Organic Carbon Deposition (mg/m²/day)", "Microbial Biomass (μg C/g sediment)"],
    [
        ["Kermadec Trench", "10,047", "14.2", "420"],
        ["Mariana Trench", "10,920", "8.6", "260"],
        ["Japan Trench", "7,542", "22.5", "680"],
        ["Atacama Trench", "8,055", "18.1", "540"]
    ]
)
rw2.append(make_mcq(
    "t3-rw-m2-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Hard",
    table_t3_q9 + "<br>Oceanographers studying hadal trench ecosystems hypothesize that benthic microbial biomass is driven primarily by the rate of organic carbon deposition funneling down steep trench slopes rather than by absolute ocean depth.",
    "Which choice best uses data from the table to support the oceanographers' hypothesis?",
    [
        "The Japan Trench had the highest organic carbon deposition (22.5 mg/m²/day) and the highest microbial biomass (680 μg C/g) despite being the shallowest trench in the sample (7,542 m), whereas the deepest trench (Mariana) had lower deposition and biomass.",
        "The Mariana Trench had the lowest microbial biomass because it experienced higher hydrostatic pressure than the Kermadec Trench.",
        "The Kermadec Trench had a higher deposition rate than the Atacama Trench despite having greater ocean depth.",
        "All four trenches had identical rates of microbial respiration across all hadal depth intervals."
    ],
    "A",
    "Choice A is correct. The hypothesis states that carbon deposition, not absolute depth, drives biomass. Showing the shallowest trench had the highest deposition and highest biomass (Japan Trench) directly supports this."
))

rw2.append(make_mcq(
    "t3-rw-m2-q10", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "Historian Peter Heather argues that the military logistics of the late Roman Empire were transformed not by barbarian invasions, but by internal reorganization that prioritized mobile field armies (<i>comitatenses</i>) stationed near regional capitals over static border garrisons (<i>limitanei</i>).",
    "Which historical record would most directly support Heather's argument?",
    [
        "An imperial edict reallocating grain supplies and weapons production from frontier Rhine outposts to support central cavalry legions garrisoned in Milan.",
        "A travel itinerary documenting a merchant trading amber along the Baltic coast in 350 CE.",
        "A military handbook detailing how legionaries sharpened bronze swords before the Punic Wars.",
        "A municipal census showing that the population of Rome declined following a malaria outbreak."
    ],
    "A",
    "Choice A is correct. Reallocating grain and weapons from frontier border outposts to central mobile cavalry legions in Milan directly illustrates the shift from border garrisons to mobile field armies."
))

rw2.append(make_mcq(
    "t3-rw-m2-q11", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Neurobiologists studying adult neurogenesis in the subgranular zone of the dentate gyrus found that voluntary running on exercise wheels increased the proliferation of neural progenitor cells in adult mice threefold. When researchers blocked brain-derived neurotrophic factor (BDNF) receptors in the hippocampus using a selective antagonist, running no longer increased progenitor cell proliferation or improved performance on a spatial pattern separation maze. However, administering BDNF directly into the hippocampus of sedentary control mice replicated the neurogenic benefits of running. This result strongly suggests that _____.",
    "Which choice most logically completes the text?",
    [
        "BDNF signaling is both necessary and sufficient to mediate the neurogenic and cognitive benefits induced by physical exercise",
        "voluntary exercise induces neurogenesis by directly activating motor neurons in the spinal cord without brain involvement",
        "hippocampal neurogenesis is unrelated to mammalian spatial learning and pattern separation performance",
        "sedentary lifestyles permanently disable all receptor sites for neurotrophic factors in the brain"
    ],
    "A",
    "Choice A is correct. Blocking BDNF stopped running from helping (necessary), and injecting BDNF in sedentary mice reproduced the benefit (sufficient). Thus BDNF is both necessary and sufficient."
))

rw2.append(make_mcq(
    "t3-rw-m2-q12", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "In astrophysics, the cosmic microwave background (CMB) radiation provides an observational snapshot of the universe approximately 380,000 years after the Big Bang. Prior to this epoch, the universe was an opaque, ionized plasma of photons, protons, and electrons undergoing continuous Thomson scattering. As the cosmos expanded and cooled below 3,000 Kelvin, electrons bound to protons to form neutral hydrogen atoms in a process known as recombination. With free electrons eliminated, photons decoupled from matter and traveled unimpeded across space, creating the primordial radiation we observe today.",
    "Which choice best summarizes the central idea of the text?",
    [
        "The cosmic microwave background formed when the universe cooled sufficiently for neutral hydrogen atoms to form, allowing photons to travel freely through space.",
        "Thomson scattering continues to prevent astronomers from observing galaxies beyond our local group.",
        "Recombination converted all hydrogen in the early universe into helium and lithium nuclei.",
        "The Big Bang occurred when cosmic microwave background radiation condensed into dense planetary matter."
    ],
    "A",
    "Choice A is correct. The text explains that cooling allowed electrons to bind to protons (recombination), freeing photons from Thomson scattering to travel unimpeded as the CMB."
))

rw2.append(make_mcq(
    "t3-rw-m2-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "In behavioral finance, the 'disposition effect' refers to the tendency of investors to sell winning investments too quickly to lock in gains while holding losing investments too long in the hope of breaking even. Researchers analyzing trading accounts observed that investors sold winning stocks at a rate 50 percent higher than losing stocks. However, when brokerage accounts were modified to automatically calculate and display the capital gains tax liability accrued from selling winners alongside the tax-deductible benefits of realizing losses, the disparity between selling winners and losers was cut in half. This finding implies that the disposition effect _____.",
    "Which choice most logically completes the text?",
    [
        "can be substantially mitigated when salient fiscal information counterbalances emotional loss aversion",
        "is caused entirely by mathematical illiteracy among novice retail investors",
        "disappears completely only when algorithmic trading platforms execute trades autonomously",
        "persists unchanged regardless of changes in tax policy or visual fee disclosures"
    ],
    "A",
    "Choice A is correct. Displaying salient tax liability and loss benefits halved the effect, showing that clear fiscal information mitigates the emotionally driven disposition effect."
))

rw2.append(make_mcq(
    "t3-rw-m2-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "During the Gilded Age, the rapid expansion of the American railway network necessitated the creation of standardized time zones in 1883. Previously, thousands of towns operated on local solar noon, resulting in over three hundred conflicting local times across the United States that caused train collisions and scheduling chaos. The railway companies unilaterally divided the nation into four standard time zones (Eastern, Central, Mountain, Pacific), which was so widely adopted by businesses that the United States Congress formally codified it into federal law thirty-five years later in the Standard Time Act of 1918.",
    "According to the text, what initially spurred the creation of standardized time zones?",
    [
        "The need to eliminate dangerous scheduling confusion and collisions across the expanding railway network.",
        "A mandate issued by the United States Congress during the Civil War.",
        "The invention of atomic clocks capable of measuring nanosecond variations in solar noon.",
        "Petitions from agricultural cooperatives seeking uniform market opening hours."
    ],
    "A",
    "Choice A is correct. The passage explicitly states that three hundred conflicting solar times caused scheduling chaos and train collisions, necessitating railway standardization."
))

# 15-21 Standard English Conventions
rw2.append(make_mcq(
    "t3-rw-m2-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
    "The botanical taxonomy committee recognized three distinct sub-species: the northern coastal fir, which thrives in humid _____ the alpine dwarf fir, found above the timberline; and the valley fir, adapted to semi-arid foothills.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["fogs;", "fogs,", "fogs—", "fogs:"]
    ,"A",
    "Choice A is correct. In a list where items contain internal commas (e.g. 'the northern coastal fir, which thrives in humid fogs'), semicolons must separate the items."
))

rw2.append(make_mcq(
    "t3-rw-m2-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The chief crystallographer noted that the mineral's crystalline lattice—an intricate arrangement of silicate tetrahedra and hydrated iron _____ had remained stable despite exposure to severe thermal stress.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["oxides—", "oxides,", "oxides;", "oxides"]
    ,"A",
    "Choice A is correct. An em-dash is required to close the parenthetical descriptor that opened with '—an intricate arrangement of silicate tetrahedra and hydrated iron oxides—'."
))

rw2.append(make_mcq(
    "t3-rw-m2-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "A collection of illuminated manuscripts from 14th-century Flanders _____ on public display at the National Gallery of Art through next November.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["is", "are", "were", "have been"],
    "A",
    "Choice A is correct. The head subject is 'A collection' (singular), which takes the singular verb 'is'."
))

rw2.append(make_mcq(
    "t3-rw-m2-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Hard",
    "Formulated to resist microbial degradation and mechanical weathering in deep subterranean tunnels, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the polymer coating was applied to the subway system's structural steel reinforcements.",
        "engineers applied the polymer coating to the subway system's structural steel reinforcements.",
        "the subway system's structural steel reinforcements were protected by the polymer coating.",
        "it was decided that the polymer coating should be applied to structural steel reinforcements."
    ],
    "A",
    "Choice A is correct. The introductory participial modifier 'Formulated to resist microbial degradation...' must logically modify 'the polymer coating'."
))

rw2.append(make_mcq(
    "t3-rw-m2-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "Early evolutionary theorists believed that flight in birds evolved from the ground up through cursorial running; _____ the discovery of feathered dinosaurs with arboreal adaptations suggested that glides from trees initiated avian flight.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["subsequently,", "similarly,", "furthermore,", "in other words,"],
    "A",
    "Choice A is correct. 'Subsequently,' signals the later chronological discovery that challenged and refined the earlier running hypothesis."
))

rw2.append(make_mcq(
    "t3-rw-m2-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Each of the forensic accountants presented _____ audit findings to the grand jury investigating securities fraud.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["their", "its", "they're", "it's"],
    "B",
    "Choice B is correct. 'Each' is singular, referring to individual accountants or entity, requiring the singular possessive pronoun 'his or her' or singular 'its' when referring to an individual/office."
))
# Let's adjust q20 choice to standard gender-neutral/singular testing on SAT:
rw2[-1]["choices"] = [{"letter": "A", "text": "his or her"}, {"letter": "B", "text": "their"}, {"letter": "C", "text": "they're"}, {"letter": "D", "text": "its"}]
rw2[-1]["correctAnswer"] = "A"
rw2[-1]["explanation"] = "Choice A is correct. 'Each' is an indefinite pronoun that is grammatically singular, requiring the singular possessive pronoun 'his or her'."

rw2.append(make_mcq(
    "t3-rw-m2-q21", DOMAINS["RW"]["CONV"], "Parallel Structure", "Medium",
    "The environmental conservation initiative seeks to restore native salt marshes, eradicate invasive phragmites reeds, and _____ public awareness regarding coastal storm surge vulnerability.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["elevate", "elevating", "to elevate", "elevates"],
    "A",
    "Choice A is correct. The parallel verb series consists of base infinitives: 'restore...', 'eradicate...', and 'elevate...'."
))

# 22-24 Transitions
rw2.append(make_mcq(
    "t3-rw-m2-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "Early astronomers believed the solar system was enclosed within a fixed celestial sphere of stars. _____, Nicolaus Copernicus demonstrated that Earth orbits the Sun, initiating the scientific revolution.",
    "Which choice completes the text with the most logical transition?",
    ["In 1543, however,", "Consequently,", "In addition,", "For example,"],
    "A",
    "Choice A is correct. 'In 1543, however,' introduces the pivotal historical moment that overturned the ancient fixed-sphere paradigm."
))

rw2.append(make_mcq(
    "t3-rw-m2-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "Synthetic nitrogen fertilizers drastically increased global agricultural crop yields throughout the 20th century. _____, agricultural runoff into river basins has caused massive marine eutrophication and hypoxic dead zones in coastal waters.",
    "Which choice completes the text with the most logical transition?",
    ["At the same time,", "In other words,", "Therefore,", "Similarly,"],
    "A",
    "Choice A is correct. 'At the same time,' sets up the concurrent unintended negative consequence (eutrophication) alongside the massive agricultural benefit."
))

rw2.append(make_mcq(
    "t3-rw-m2-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "The sculptor chose Carrara marble for its fine grain and subtle translucence. _____, the stone possesses an elasticity that permits carving delicate figurative drapery without fracturing.",
    "Which choice completes the text with the most logical transition?",
    ["Furthermore,", "On the contrary,", "Rather,", "Instead,"],
    "A",
    "Choice A is correct. 'Furthermore,' introduces an additional physical characteristic (elasticity for fine carving) that supports the sculptor's choice of material."
))

# 25-27 Rhetorical Synthesis
rw2.append(make_mcq(
    "t3-rw-m2-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Antoni Gaudí was a visionary Catalan architect known for designing the Sagrada Família in Barcelona.",
        "To calculate structural loads, Gaudí constructed upside-down physical models using hanging weighted strings.",
        "Hanging strings naturally form perfect catenary curves under gravity.",
        "When inverted, these catenary curves become arches that experience pure compression and zero tensile strain.",
        "This ingenious method allowed Gaudí to design soaring stone columns without needing exterior flying buttresses."
    ]),
    "The student wants to explain how Gaudí's physical modeling method influenced his architectural designs. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "By building upside-down hanging string models that formed natural catenary curves, Gaudí was able to design soaring stone columns that eliminated the need for external flying buttresses.",
        "Antoni Gaudí was a celebrated Catalan architect who devoted decades of his career to designing the Sagrada Família in Barcelona.",
        "Hanging weighted strings naturally form catenary curves, which experience pure compression when inverted into stone arches.",
        "Flying buttresses were exterior architectural supports traditionally utilized by medieval Gothic cathedral builders."
    ],
    "A",
    "Choice A is correct. It directly fulfills the prompt by connecting the modeling method (upside-down hanging strings) to the resulting design feature (soaring columns with no external flying buttresses)."
))

rw2.append(make_mcq(
    "t3-rw-m2-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "The James Webb Space Telescope (JWST) detected galaxy JADES-GS-z14-0 in early 2024.",
        "The galaxy has a confirmed spectroscopic redshift of z = 14.32.",
        "This redshift indicates the galaxy existed approximately 290 million years after the Big Bang.",
        "It is surprisingly luminous and massive for such an early cosmological epoch.",
        "This discovery challenges theoretical models that predicted early galaxies would be tiny and faint."
    ]),
    "The student wants to highlight why the discovery of JADES-GS-z14-0 surprised astrophysicists. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Existing approximately 290 million years after the Big Bang, JADES-GS-z14-0 surprised astrophysicists with its unexpected brightness and mass, challenging theoretical models of early galaxy formation.",
        "In early 2024, the James Webb Space Telescope detected galaxy JADES-GS-z14-0 at a redshift of z = 14.32.",
        "Redshift measurements allow cosmologists to calculate the historical epoch in which distant celestial objects formed.",
        "Astrophysicists rely on the James Webb Space Telescope to observe celestial bodies that emitted light in the early universe."
    ],
    "A",
    "Choice A is correct. It directly addresses the prompt's goal by emphasizing why the galaxy surprised scientists (unexpected brightness and mass that challenged early formation models)."
))

rw2.append(make_mcq(
    "t3-rw-m2-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Hydrothermal vent mineral chimneys are known as 'black smokers' and 'white smokers'.",
        "Black smokers emit fluids exceeding 350°C rich in iron sulfides, which precipitate as dark mineral clouds.",
        "White smokers emit cooler fluids (under 300°C) rich in barium, calcium, and silicon compounds.",
        "White smoker chimneys precipitate lighter-colored anhydrite and silica crystals.",
        "Both chimney types support distinct microbiomes adapted to differing thermal and geochemical regimes."
    ]),
    "The student wants to contrast the mineral emissions of black smokers with those of white smokers. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "While black smokers emit fluids exceeding 350°C rich in dark iron sulfides, white smokers emit cooler fluids rich in barium, calcium, and silica compounds that precipitate light-colored crystals.",
        "Deep-sea hydrothermal mineral chimneys are categorized as either black smokers or white smokers depending on fluid properties.",
        "Both black and white smokers provide thermal and geochemical energy that sustains specialized deep-sea bacterial microbiomes.",
        "White smoker chimneys precipitate anhydrite and silica crystals in ocean waters that do not exceed 300°C."
    ],
    "A",
    "Choice A is correct. It directly contrasts the two types of chimneys: black smokers with >350°C iron sulfides vs white smokers with cooler fluids rich in barium, calcium, and silica."
))

print(f"Test 3 RW Module 2 ready: {len(rw2)} questions.")
