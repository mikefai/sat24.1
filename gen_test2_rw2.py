# gen_test2_rw2.py - Practice Test 2 RW Module 2 (27 questions)
import json
from generate_suite_all import DOMAINS, make_mcq, make_bullet_notes, make_dual_passage, make_table

rw2 = []

# 1-4 Advanced Words in Context
rw2.append(make_mcq(
    "t2-rw-m2-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Because the legal defense team inundated the courtroom with thousands of pages of _____ financial spreadsheets that bore no relevance to the embezzlement charges, the presiding judge ordered sanctions for dilatory conduct.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["superfluous", "indispensable", "lucid", "meticulous"],
    "A",
    "Choice A is correct. 'Superfluous' means unnecessary or exceeding what is needed. Piles of spreadsheets that 'bore no relevance' to the charges were superfluous."
))

rw2.append(make_mcq(
    "t2-rw-m2-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The chief software architect was notoriously _____ regarding code hygiene, routinely rejecting pull requests for minor indentation discrepancies or variable naming formatting that fell short of the repository's strict aesthetic guidelines.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["fastidious", "complacent", "impetuous", "garrulous"],
    "A",
    "Choice A is correct. 'Fastidious' means very attentive to accuracy, detail, and cleanliness. Rejecting code for tiny indentation inconsistencies exemplifies fastidiousness."
))

rw2.append(make_mcq(
    "t2-rw-m2-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Environmental economists warned that introducing water subsidies during an active drought would only _____ regional aquifer depletion by removing the financial incentive for agricultural irrigation efficiency.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["exacerbate", "ameliorate", "adjudicate", "circumvent"],
    "A",
    "Choice A is correct. 'Exacerbate' means to make a problem or bad situation worse. Water subsidies would worsen aquifer depletion."
))

rw2.append(make_mcq(
    "t2-rw-m2-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "The hiring committee emphasized that compensation packages would be strictly _____ with each candidate's years of specialized technical experience and measurable leadership accomplishments.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["commensurate", "incongruous", "peripheral", "transitory"],
    "A",
    "Choice A is correct. 'Commensurate' means corresponding in size or degree; in proportion. Compensation matching experience is commensurate."
))

# 5-8 Cross-Text Connections & Structure
rw2.append(make_mcq(
    "t2-rw-m2-q5", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Art historian Paolo Rossi argues that Italian Renaissance art flourished primarily because elite civic patrons (such as the Medici family) provided sustained financial commissions that liberated master painters from commercial market anxieties, enabling radical aesthetic experimentation.",
        "Cultural sociologist Elena Greco counters that aristocratic patronage frequently constrained artistic autonomy, as wealthy benefactors enforced rigid theological iconography and demanded flattering self-portraits, whereas independent merchant guilds in Venice fostered far more innovative secular genre painting."
    ),
    "Based on the texts, how does Greco (Text 2) view the influence of elite patronage discussed by Rossi (Text 1)?",
    [
        "She views elite patronage as a restrictive force that often stifled artistic independence rather than fostering unbounded aesthetic freedom.",
        "She agrees that aristocratic families in Florence completely eliminated theological censorship in Renaissance painting.",
        "She demonstrates that merchant guilds in Venice provided higher financial stipends than the Medici family.",
        "She argues that secular genre painting originated in Florence rather than in the Venetian Republic."
    ],
    "A",
    "Choice A is correct. While Rossi argues patronage liberated artists, Greco contends it constrained autonomy by imposing rigid iconography and self-flattery."
))

rw2.append(make_mcq(
    "t2-rw-m2-q6", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "In evolutionary biology, Batesian mimicry occurs when a harmless organism evolves physical warning signals resembling those of a noxious or venomous model species, thereby deterring predators. <u>However, this evolutionary strategy is inherently frequency-dependent: if the mimic population expands to outnumber the toxic model, predators encounter harmless mimics more frequently, weakening the protective conditioned avoidance association.</u>",
    "Which choice best describes the function of the underlined sentence in the text as a whole?",
    [
        "It identifies an ecological limitation that constrains the population density of Batesian mimics.",
        "It provides evidence that toxic model species eventually evolve mimicry to confuse predators.",
        "It refutes the claim that Batesian mimicry provides any defensive advantage against predators.",
        "It describes a newly discovered species that exhibits both Batesian and Müllerian mimicry."
    ],
    "A",
    "Choice A is correct. The underlined sentence explains that if mimic numbers grow too high, the warning signal stops working, which represents an ecological constraint on mimic density."
))

rw2.append(make_mcq(
    "t2-rw-m2-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Hard",
    "Climatologists investigating urban heat island (UHI) phenomena have documented substantial microclimatic temperature elevations in densely built metropolitan districts compared to surrounding rural hinterlands. <u>While replacing dark asphalt surfaces with high-albedo reflective coatings effectively suppresses daytime surface temperatures, it can inadvertently elevate pedestrian thermal discomfort at street level by increasing upward reflected shortwave radiation.</u>",
    "Which choice best describes the function of the underlined sentence?",
    [
        "It highlights an unintended consequence of an otherwise effective urban cooling mitigation strategy.",
        "It proposes an alternative architectural coating made entirely of biological plant polymers.",
        "It disputes the hypothesis that asphalt surfaces absorb more solar radiation than rural vegetation.",
        "It summarizes municipal zoning policies regulating rooftop reflectivity in European capitals."
    ],
    "A",
    "Choice A is correct. The underlined sentence introduces an unintended negative side-effect (increased reflected radiation hurting pedestrians) of a strategy that otherwise successfully cools surfaces."
))

rw2.append(make_mcq(
    "t2-rw-m2-q8", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "Political scientist Thomas Brody argues that term limits for state legislators revitalize democratic governance by ensuring regular turnover, dismantling entrenched incumbent patronage networks, and encouraging citizen-legislators.",
        "Public policy researcher Sarah Vance contends that legislative term limits weaken legislative effectiveness by prematurely expelling experienced lawmakers, shifting policy expertise and drafting power into the hands of unelected lobbyists and permanent bureaucratic staffers."
    ),
    "Based on the texts, how would Vance (Text 2) most likely respond to Brody's argument in Text 1 regarding the benefits of regular turnover?",
    [
        "By pointing out that constant legislative turnover inadvertently empowers unelected lobbyists who possess institutional memory.",
        "By asserting that incumbent politicians always have lower re-election rates than non-incumbent challengers.",
        "By proving that term-limited legislators vote more frequently on fiscal appropriation bills.",
        "By agreeing that legislative turnover completely eliminates the influence of special interest groups."
    ],
    "A",
    "Choice A is correct. Vance directly counters Brody's optimism by showing that constant turnover causes loss of expertise and transfers power to unelected lobbyists."
))

# 9-14 Information and Ideas
table_t2_q9 = make_table(
    ["Reef Location", "Mean Sea Temp (°C)", "Bleaching Extent (%)", "Symbiodiniaceae Density (cells/cm²)"],
    [
        ["Reef A (Control)", "27.5", "4", "1.8 × 10⁶"],
        ["Reef B (Moderate Heat)", "29.2", "38", "0.9 × 10⁶"],
        ["Reef C (Severe Heat)", "31.0", "82", "0.2 × 10⁶"],
        ["Reef D (Heat + Shade)", "31.0", "44", "0.8 × 10⁶"]
    ]
)
rw2.append(make_mcq(
    "t2-rw-m2-q9", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Hard",
    table_t2_q9 + "<br>Marine biologists investigating coral bleaching hypothesize that elevated water temperatures expel photosynthetic dinoflagellate symbionts (Symbiodiniaceae), leading to loss of coral pigmentation. Furthermore, they hypothesize that artificial solar shading can significantly mitigate symbiont expulsion even during high thermal stress.",
    "Which choice best uses data from the table to support both parts of the biologists' hypothesis?",
    [
        "Bleaching extent rose from 4% in Reef A to 82% in Reef C as temperature increased to 31.0°C (with symbiont density falling to 0.2 × 10⁶), but artificial shading in Reef D at 31.0°C kept bleaching at 44% and symbiont density at 0.8 × 10⁶.",
        "Reef B experienced less bleaching than Reef C because water temperatures at Reef B were identical to Reef A.",
        "Symbiodiniaceae density was identical across Reef A and Reef D despite substantial differences in sea temperature.",
        "Reef D exhibited higher coral bleaching than Reef C because shading reduced light needed for coral respiration."
    ],
    "A",
    "Choice A is correct. It supports both claims: higher heat drastically increases bleaching and drops symbiont density (Reef A vs C), while artificial shading at 31.0°C preserves higher symbiont density and cuts bleaching in half (Reef C vs D)."
))

rw2.append(make_mcq(
    "t2-rw-m2-q10", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "In her study of 18th-century English epistolary novels, literary critic Dr. Aris Thorne argues that the epistolary format (novels composed of letters) served a crucial feminist function by granting female protagonists complete, unmediated authority over the narration of their own psychological experiences.",
    "Which statement from an 18th-century epistolary novel would most directly support Thorne's argument?",
    [
        "\"In these private letters to thee, my dearest friend, I write with my own hand and untamed voice, free from my guardian's censorship, revealing the true tumult of my secret soul.\"",
        "\"The postal carrier arrives promptly at six in the evening on Tuesdays and Fridays to deliver the county gazette.\"",
        "\"We attended the London masquerade ball dressed in silk garments imported from the West Indies.\"",
        "\"My brother insists that all estates descend exclusively through the elder male line of our family.\""
    ],
    "A",
    "Choice A is correct. The protagonist explicitly describes writing in her own voice without her guardian's censorship to express her inner psychological truth, directly matching Thorne's claim."
))

rw2.append(make_mcq(
    "t2-rw-m2-q11", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "In paleoclimatology, the ratio of oxygen-18 to oxygen-16 ($^{18}\\text{O}/^{16}\\text{O}$) preserved in fossil foraminifera shells reflects past global ice volume. Because water molecules containing lighter $^{16}\\text{O}$ evaporate more readily from oceans and become locked in continental ice sheets during glacial epochs, the remaining seawater becomes enriched in heavier $^{18}\\text{O}$. Deep-sea sediment cores extracted from the North Atlantic reveal pronounced spikes in benthic $^{18}\\text{O}/^{16}\\text{O}$ ratios occurring at roughly 100,000-year intervals over the last million years. This stratigraphic pattern implies that _____.",
    "Which choice most logically completes the text?",
    [
        "major continental glaciations occurred cyclically roughly every 100,000 years over the past million years",
        "oceanic water temperatures remained completely constant throughout the entirety of the Pleistocene epoch",
        "atmospheric carbon dioxide levels reached their historical maxima during periods of elevated $^{18}\\text{O}$ concentration",
        "foraminifera shells ceased to calcify during warm interglacial climatic periods"
    ],
    "A",
    "Choice A is correct. High $^{18}\\text{O}/^{16}\\text{O}$ indicates large continental ice sheets; spikes occurring at 100,000-year intervals imply that glaciations followed a 100,000-year cycle."
))

rw2.append(make_mcq(
    "t2-rw-m2-q12", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "The development of liquid biopsy technology has transformed oncology diagnostics. Traditional tissue biopsies require invasive surgical excision of tumor tissue, which carries clinical risk and fails to capture spatial genetic heterogeneity across metastatic sites. Liquid biopsies, by contrast, isolate circulating tumor DNA (ctDNA) shed into peripheral blood streams. This non-invasive blood test allows clinicians to track real-time tumor genetic evolution and detect emergent therapy resistance mutations months before macroscopic lesions appear on radiological scans.",
    "Which choice best summarizes the central idea of the text?",
    [
        "Liquid biopsies provide a non-invasive means to detect ctDNA and monitor tumor evolution earlier and more comprehensively than surgical biopsies.",
        "Radiological scans have become completely obsolete in modern oncological clinical practice.",
        "Surgical excision remains the only method capable of detecting metastatic tumor mutations.",
        "Circulating tumor DNA is present in equal concentrations across healthy and cancerous tissues."
    ],
    "A",
    "Choice A is correct. The text highlights that liquid biopsies provide non-invasive blood monitoring of ctDNA, catching tumor evolution and resistance earlier than surgical biopsies or scans."
))

rw2.append(make_mcq(
    "t2-rw-m2-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Cognitive linguists examining grammatical gender systems tested whether language shapes conceptual thought (the linguistic relativity hypothesis). German speakers, for whom the word 'key' (<i>der Schlüssel</i>) is grammatically masculine, described keys using adjectives like 'heavy,' 'jagged,' and 'metal.' Spanish speakers, for whom 'key' (<i>la llave</i>) is grammatically feminine, described keys using adjectives like 'intricate,' 'little,' and 'golden.' When the experiment was repeated using an artificial language where objects were assigned arbitrary novel grammatical markers, participants exhibited similar gendered descriptive biases after only two hours of immersion. This finding indicates that _____.",
    "Which choice most logically completes the text?",
    [
        "grammatical category assignments can rapidly bias cognitive object perception even in the absence of long-term cultural conditioning",
        "linguistic relativity applies exclusively to native speakers of Romance and Germanic language families",
        "participants are incapable of learning artificial grammatical gender systems in laboratory settings",
        "adjective selection is determined entirely by physical tactile interaction with experimental objects"
    ],
    "A",
    "Choice A is correct. Since participants showed gendered descriptive biases after only two hours in an artificial language, grammatical categories rapidly bias cognitive perception without needing lifetime cultural conditioning."
))

rw2.append(make_mcq(
    "t2-rw-m2-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "In quantum computing, superconducting qubits must be maintained at millikelvin temperatures inside dilution refrigerators to minimize thermal noise that causes qubit decoherence. However, scaling quantum processors to millions of qubits creates an 'interconnect bottleneck': the physical coaxial cables carrying microwave control pulses from room-temperature electronics into the cryostat conduct too much parasitic heat into the system, threatening thermal equilibrium.",
    "According to the text, what challenge arises when scaling superconducting quantum computers?",
    [
        "Control cables conduct unwanted ambient heat into the cryostat, disrupting the low temperatures needed for qubit stability.",
        "Superconducting qubits cease to conduct electrical current at temperatures approaching absolute zero.",
        "Microwave control pulses lose signal strength when passing through dilution refrigerators.",
        "Dilution refrigerators consume all available electrical power in modern computing data centers."
    ],
    "A",
    "Choice A is correct. The passage specifies that physical coaxial cables carrying microwave signals conduct parasitic heat into the cryostat, creating a thermal scaling bottleneck."
))

# 15-21 Standard English Conventions
rw2.append(make_mcq(
    "t2-rw-m2-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Hard",
    "The archival team cataloged three collections: Dr. Vance's personal letters from the Spanish Civil _____ Professor Thorne's audio recordings of Appalachian folk songs; and Magistrate Lin's colonial court transcripts.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["War;", "War,", "War—", "War"]
    ,"A",
    "Choice A is correct. Semicolons are required to separate items in a complex series when the items themselves contain internal descriptive phrasing or parallel semicolon structure is established."
))

rw2.append(make_mcq(
    "t2-rw-m2-q16", DOMAINS["RW"]["CONV"], "Punctuation", "Hard",
    "The lead biochemist explained that the newly synthesized enzyme—an engineered esterase derived from deep-sea vent _____ could degrade polyethylene terephthalate (PET) plastic in under forty-eight hours.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["bacteria—", "bacteria,", "bacteria;", "bacteria"]
    ,"A",
    "Choice A is correct. An em-dash is required to close the parenthetical appositive that began with '—an engineered esterase derived from deep-sea vent bacteria—'."
))

rw2.append(make_mcq(
    "t2-rw-m2-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Medium",
    "A meticulous analysis of the Roman amphorae fragments discovered in the harbor basin _____ that coastal merchant vessels carried olive oil and wine from Hispania to Britannia throughout the second century CE.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["indicates", "indicate", "have indicated", "are indicating"],
    "A",
    "Choice A is correct. The head subject is 'A meticulous analysis' (singular), requiring the singular verb 'indicates'."
))

rw2.append(make_mcq(
    "t2-rw-m2-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Hard",
    "Designed to withstand Category 5 hurricane winds and corrosive saltwater spray, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "the offshore wind turbine features reinforced carbon-fiber blades and a galvanized steel foundation.",
        "engineers built the offshore wind turbine using reinforced carbon-fiber blades and galvanized steel.",
        "the foundation of the offshore wind turbine was constructed from galvanized steel and carbon fiber.",
        "it was determined that the offshore wind turbine could operate during severe ocean storms."
    ],
    "A",
    "Choice A is correct. The introductory modifier 'Designed to withstand Category 5 hurricane winds...' must logically modify 'the offshore wind turbine'."
))

rw2.append(make_mcq(
    "t2-rw-m2-q19", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "Linguists originally hypothesized that the Etruscan language was closely related to early Indo-European tongues; _____ phonological and morphological evidence confirmed that it belongs to an isolated, non-Indo-European language family.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["subsequently,", "furthermore,", "similarly,", "for example,"],
    "A",
    "Choice A is correct. 'Subsequently,' indicates that later chronological discoveries disproved the initial hypothesis."
))

rw2.append(make_mcq(
    "t2-rw-m2-q20", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "Neither the lead architect nor the project managers were willing to compromise _____ standards regarding structural earthquake resilience.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["their", "its", "they're", "it's"],
    "A",
    "Choice A is correct. In a 'neither... nor' structure where the second subject is plural ('project managers'), the plural pronoun 'their' is required."
))

rw2.append(make_mcq(
    "t2-rw-m2-q21", DOMAINS["RW"]["CONV"], "Parallel Structure", "Medium",
    "The new regulatory guidelines mandate that financial institutions encrypt client transaction data, conduct quarterly vulnerability audits, and _____ suspicious account activity to federal monitors immediately.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["report", "reporting", "to report", "reports"],
    "A",
    "Choice A is correct. The parallel verb series consists of base verbs: 'encrypt...', 'conduct...', and 'report...'."
))

# 22-24 Transitions
rw2.append(make_mcq(
    "t2-rw-m2-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "Early quantum physicists assumed that electrons orbited atomic nuclei in fixed, planetary circular paths. _____, Erwin Schrödinger demonstrated that electrons exist in probabilistic three-dimensional wave-function orbitals.",
    "Which choice completes the text with the most logical transition?",
    ["In 1926, however,", "Consequently,", "In addition,", "For instance,"],
    "A",
    "Choice A is correct. 'In 1926, however,' introduces the contrasting breakthrough that replaced the erroneous planetary model with Schrödinger's wave-function model."
))

rw2.append(make_mcq(
    "t2-rw-m2-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "The rare-earth mineral neodymium is indispensable for manufacturing powerful permanent magnets used in electric vehicle motors. _____, global supply chains remain vulnerable to price spikes because mining and refining operations are concentrated in a handful of geographical regions.",
    "Which choice completes the text with the most logical transition?",
    ["Accordingly,", "In contrast,", "Nevertheless,", "Conversely,"],
    "A",
    "Choice A is correct. 'Accordingly,' shows the logical cause-and-effect link: because neodymium is critical for EV magnets, geographic concentration creates supply chain vulnerabilities."
))

rw2.append(make_mcq(
    "t2-rw-m2-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Hard",
    "The museum's new wing was constructed using translucent alabaster panels that filter daylight into the central gallery. _____, the stone panels provide acoustic dampening that shields visitors from the clamor of adjacent city traffic.",
    "Which choice completes the text with the most logical transition?",
    ["Equally important,", "On the contrary,", "In other words,", "Instead,"],
    "A",
    "Choice A is correct. 'Equally important,' smoothly introduces an additional functional benefit (acoustic insulation) alongside the visual benefit (light filtering)."
))

# 25-27 Rhetorical Synthesis
rw2.append(make_mcq(
    "t2-rw-m2-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "The ancient Maya script consists of over 800 phonetic glyphs and logograms.",
        "For centuries, Western scholars mistakenly believed Maya glyphs were purely pictographic symbols.",
        "In the 1950s, Russian linguist Yuri Knorozov demonstrated that the glyphs functioned syllabically.",
        "Knorozov matched glyph combinations with spoken Yucatec Maya grammar and vocabulary.",
        "His breakthrough enabled epigraphers to decipher more than 90 percent of surviving Maya inscriptions."
    ]),
    "The student wants to emphasize the impact of Yuri Knorozov's discovery on Maya epigraphy. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "By proving in the 1950s that Maya glyphs functioned syllabically, Yuri Knorozov enabled scholars to decipher over 90 percent of surviving Maya inscriptions.",
        "For centuries, Western scholars erroneously believed that the Maya script of over 800 glyphs was purely pictographic.",
        "Yuri Knorozov compared ancient Maya writing with spoken Yucatec Maya vocabulary in the 1950s.",
        "The Maya writing system consists of both phonetic syllabic glyphs and individual logograms."
    ],
    "A",
    "Choice A is correct. It directly addresses the goal: showing the impact of Knorozov's discovery (enabling the decipherment of over 90% of surviving inscriptions)."
))

rw2.append(make_mcq(
    "t2-rw-m2-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Quantum dots are semiconductor nanocrystals measuring only 2 to 10 nanometers in diameter.",
        "When stimulated by light or electricity, quantum dots emit precise, pure colors.",
        "The emitted wavelength depends strictly on the physical size of the nanocrystal.",
        "Smaller dots emit high-energy blue light, whereas larger dots emit lower-energy red light.",
        "They are used in high-end television displays and medical bio-imaging probes."
    ]),
    "The student wants to explain the relationship between a quantum dot's size and its light emission. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "The color wavelength emitted by a quantum dot depends directly on its physical size, with smaller dots emitting blue light and larger dots emitting red light.",
        "Measuring between 2 and 10 nanometers, quantum dots are microscopic semiconductor crystals used in television screens and bio-imaging.",
        "When excited by electricity or light, semiconductor nanocrystals emit extraordinarily pure color spectrums.",
        "Quantum dots are versatile nanoscale materials that have applications ranging from commercial electronics to biomedical diagnostics."
    ],
    "A",
    "Choice A is correct. It directly fulfills the goal by describing the specific size-to-light relationship (smaller = blue light, larger = red light)."
))

rw2.append(make_mcq(
    "t2-rw-m2-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Biochar is a stable, carbon-rich charcoal produced by heating biomass in an oxygen-deprived environment (pyrolysis).",
        "When buried in agricultural soils, biochar locks carbon underground for hundreds of years.",
        "Unlike decomposing organic plant matter, which releases CO₂ back into the atmosphere, biochar resists microbial breakdown.",
        "Additionally, its porous structure retains soil moisture and boosts nutrient retention for crops."
    ]),
    "The student wants to contrast biochar with decomposing plant matter regarding carbon release. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "While decomposing plant matter releases CO₂ back into the atmosphere, biochar resists microbial breakdown, sequestering carbon in soil for hundreds of years.",
        "Biochar is a carbon-rich charcoal produced through oxygen-deprived biomass pyrolysis that improves soil moisture and crop nutrient retention.",
        "Produced through biomass pyrolysis, biochar can be incorporated into agricultural soil to enhance crop yields.",
        "Both organic mulch and biochar are soil amendments utilized by sustainable farmers to enrich depleted cropland."
    ],
    "A",
    "Choice A is correct. It directly contrasts the two: decomposing plants releasing CO₂ vs biochar resisting breakdown and locking carbon away for centuries."
))

print(f"Test 2 RW Module 2 ready: {len(rw2)} questions.")
