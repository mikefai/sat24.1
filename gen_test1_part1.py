# gen_test1.py - Test 1 with 108 questions
import json
import os
from generate_suite_all import DOMAINS, make_mcq, make_spr, make_bullet_notes, make_dual_passage, make_table

rw1 = []
rw2 = []
math1 = []
math2 = []

# ==========================================
# TEST 1 - READING & WRITING MODULE 1 (27 Qs)
# ==========================================

# 1-4 Words in Context
rw1.append(make_mcq(
    "t1-rw-m1-q1", DOMAINS["RW"]["CRAFT"], "Words in Context", "Easy",
    "In her 2021 monograph on architectural history, Dr. Elena Rostova argues that the sudden adoption of reinforced concrete in urban civic centers was neither accidental nor _____; rather, it represented a calculated response to rising industrial fire hazards and municipal insurance mandates.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["capricious", "inevitable", "pragmatic", "laudable"],
    "A",
    "Choice A is correct. 'Capricious' means impulsive or unpredictable. The sentence states the adoption was 'neither accidental nor [capricious]; rather, it represented a calculated response'."
))

rw1.append(make_mcq(
    "t1-rw-m1-q2", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "Although the ancient library catalog contained numerous gaps and obscure references, the archivist was able to _____ the provenance of the 14th-century illuminated manuscript by correlating watermarks in the rag paper with regional guild registries.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["substantiate", "repudiate", "obfuscate", "disseminate"],
    "A",
    "Choice A is correct. 'Substantiate' means to verify or establish with evidence. The archivist established the manuscript's origin by correlating paper watermarks with guild registries."
))

rw1.append(make_mcq(
    "t1-rw-m1-q3", DOMAINS["RW"]["CRAFT"], "Words in Context", "Medium",
    "The ecologist noted that while apex predators often exert a _____ influence across trophic cascades, their absence does not merely diminish local biodiversity; it fundamentally restructures the physical geomorphology of riverbanks by releasing herbivore populations from foraging pressure.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["pervasive", "peripheral", "transitory", "redundant"],
    "A",
    "Choice A is correct. 'Pervasive' means widespread and affecting all parts of an ecosystem. The passage shows apex predators affect food webs and physical riverbank structures."
))

rw1.append(make_mcq(
    "t1-rw-m1-q4", DOMAINS["RW"]["CRAFT"], "Words in Context", "Hard",
    "In public interviews, the minimalist composer was notoriously _____, often replying to expansive inquiries regarding his symphonic motifs with mere single-syllable acknowledgments or prolonged silences.",
    "Which choice completes the text with the most logical and precise word or phrase?",
    ["laconic", "loquacious", "effusive", "bellicose"],
    "A",
    "Choice A is correct. 'Laconic' means concise or using very few words. Single-syllable acknowledgments and silence are the definition of laconic."
))

# 5-8 Text Structure, Dual Passages & Purpose
rw1.append(make_mcq(
    "t1-rw-m1-q5", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "For decades, paleobotanists assumed that angiosperms (flowering plants) diversified rapidly during the mid-Cretaceous period in what Charles Darwin famously termed an 'abominable mystery.' However, recent molecular clock analyses calibrated with fossil spores from the Early Jurassic suggest that the lineage had already diverged tens of millions of years earlier than macroscopic macrofossils indicate. <u>These findings do not dispute the explosion of ecological forms in the Cretaceous, but rather recalibrate the evolutionary tempo, suggesting a prolonged cryptic phase of evolutionary experimentation.</u>",
    "Which choice best describes the function of the underlined sentence in the text as a whole?",
    [
        "It clarifies the precise nature of the challenge posed by recent molecular clock findings to established historical models.",
        "It dismisses molecular clock analysis as fundamentally incompatible with the physical macrofossil record.",
        "It introduces a third competing hypothesis regarding the geographic origins of Jurassic flowering plants.",
        "It summarizes Charles Darwin's original conceptualization of Cretaceous floral diversification."
    ],
    "A",
    "Choice A is correct. The underlined sentence clarifies how the new findings refine rather than outright contradict Darwin's model by introducing a prolonged cryptic phase."
))

rw1.append(make_mcq(
    "t1-rw-m1-q6", DOMAINS["RW"]["CRAFT"], "Cross-Text Connections", "Hard",
    make_dual_passage(
        "In a 2018 paper, economist David Miller argued that automated inventory management algorithms universally suppress inflationary price volatility by instantly matching wholesale supply orders with real-time consumer checkout demand across national retail chains.",
        "Sociologist Priya Nair examined rural grocery cooperatives and observed that algorithm-driven supply chains frequently trigger localized phantom shortages when regional freight disruptions decouple local demand signals from centralized warehouse dispatch algorithms."
    ),
    "Based on the texts, how would Nair (Text 2) most likely respond to Miller's assertion in Text 1?",
    [
        "By asserting that Miller overlooks how supply chain disruptions can cause automated systems to produce localized distribution failures.",
        "By arguing that rural retail cooperatives deliberately disable pricing algorithms during national economic recessions.",
        "By agreeing that real-time checkout monitoring eliminates consumer demand spikes in major metropolitan areas.",
        "By demonstrating that automated wholesale ordering is significantly more expensive than manual ledger tracking."
    ],
    "A",
    "Choice A is correct. While Miller asserts universal efficiency, Nair demonstrates that regional freight disruptions cause localized supply failures, refuting Miller's universal claim."
))

rw1.append(make_mcq(
    "t1-rw-m1-q7", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "Virginia Woolf's 1925 novel <i>Mrs. Dalloway</i> famously eschews conventional chronological plotting in favor of free indirect discourse, immersing readers within the uninterrupted cognitive flow of its characters over the span of a single London day. Through this structural choice, Woolf achieves a dual representation: the external, mechanized chime of Big Ben punctuating objective time, juxtaposed against the fluid, elastic interiority of human memory and psychological perception.",
    "Which choice best states the primary purpose of the text?",
    [
        "To analyze how Woolf uses narrative technique to contrast objective chronological time with subjective mental experience.",
        "To criticize the lack of traditional plot structure and chronological coherence in early 20th-century British fiction.",
        "To trace the autobiographical origins of Virginia Woolf's thematic interest in London's civic infrastructure.",
        "To compare the commercial reception of <i>Mrs. Dalloway</i> with that of other modernist novels published in 1925."
    ],
    "A",
    "Choice A is correct. The text explicitly analyzes Woolf's structural technique of contrasting objective time with subjective psychological memory."
))

rw1.append(make_mcq(
    "t1-rw-m1-q8", DOMAINS["RW"]["CRAFT"], "Text Structure and Purpose", "Medium",
    "In her analysis of Renaissance portraiture, art historian Maria Santos contends that Dutch domestic portraits served as performative instruments of civic status. Santos notes that subjects were typically rendered alongside meticulously depicted luxury trade goods—such as Persian carpets and silver navigational astrolabes—to subtly signal their merchant prosperity while maintaining an outward facade of Calvinist modesty.",
    "Which choice best describes the overall structure of the text?",
    [
        "It presents a scholarly argument and then supports it by describing specific visual elements used in the portraits.",
        "It introduces a popular misconception about Dutch portraiture and refutes it using financial receipts from 17th-century merchants.",
        "It contrasts the painting techniques of Dutch Renaissance masters with those of contemporary Italian artists.",
        "It outlines the chronological development of Calvinist religious doctrine regarding visual art."
    ],
    "A",
    "Choice A is correct. The passage presents Santos's claim (portraits served as instruments of status) and supports it by citing specific depicted trade goods (Persian carpets, astrolabes)."
))

# 9-14 Information and Ideas (Central Ideas, Inferences, Quantitative & Textual Evidence)
rw1.append(make_mcq(
    "t1-rw-m1-q9", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Easy",
    "In deep-sea hydrothermal vents, where sunlight cannot penetrate, entire biological communities thrive independently of solar energy. Instead of relying on plant-based photosynthesis, these ecosystems are anchored by chemotrophic bacteria that oxidize hydrogen sulfide dissolved in the superheated, mineral-rich effluent emitted from the seafloor crust. Tubeworms, clams, and vent shrimp harbor these bacteria endosymbiotically or graze upon bacterial mats, demonstrating that complex multicellular life can be sustained entirely through geothermal and geochemical inputs.",
    "Which choice best summarizes the central idea of the text?",
    [
        "Hydrothermal vent ecosystems are powered by chemotrophic bacteria that convert geothermal chemical compounds into organic energy.",
        "Sunlight-dependent marine organisms have gradually migrated to benthic hydrothermal fissures to escape surface predators.",
        "Tubeworms and vent shrimp produce hydrogen sulfide to generate protective thermal barriers against abyssal freezing temperatures.",
        "Photosynthesis remains an indispensable indirect biological process for all organisms residing in oceanic benthic zones."
    ],
    "A",
    "Choice A is correct. The central idea is that hydrothermal vent communities depend on chemotrophic bacteria using geothermal chemicals rather than sunlight."
))

rw1.append(make_mcq(
    "t1-rw-m1-q10", DOMAINS["RW"]["INFO"], "Inferences", "Medium",
    "Biologists studying monarch butterfly migration have long known that the insects navigate using a time-compensated sun compass, which integrates the sun's azimuth with internal circadian clocks in their antennae. In a controlled experiment, researchers placed migrating monarchs in a planetarium where magnetic fields could be artificially reversed while celestial lighting remained constant. The butterflies maintained their south-southwest trajectory regardless of magnetic disorientation; however, when the researchers shifted the artificial light-dark schedule by six hours, the butterflies' flight headings rotated by roughly 90 degrees. This finding strongly suggests that _____.",
    "Which choice most logically completes the text?",
    [
        "monarch butterflies prioritize solar and circadian cues over geomagnetic orientation during migratory navigation",
        "geomagnetic field lines serve as the exclusive sensory mechanism guiding monarchs across continental distances",
        "circadian clock proteins in antennae operate completely independently of external diurnal photoperiods",
        "monarchs rely primarily on geographic landmarks such as coastlines rather than astronomical orientation"
    ],
    "A",
    "Choice A is correct. Magnetic reversal did not alter heading, but light-cycle shifts rotated heading by 90 degrees, showing solar/circadian cues dominate."
))

table_q11 = make_table(
    ["Bird Species", "Urban Noise (dB)", "Min Frequency (Hz)", "Song Duration (s)"],
    [
        ["European Robin", "68", "2,850", "2.1"],
        ["Great Tit", "71", "3,420", "1.4"],
        ["House Sparrow", "74", "3,910", "0.9"],
        ["Song Sparrow", "65", "2,410", "2.8"]
    ]
)
rw1.append(make_mcq(
    "t1-rw-m1-q11", DOMAINS["RW"]["INFO"], "Command of Evidence: Quantitative", "Medium",
    table_q11 + "<br>Ornithologists hypothesize that urban songbirds modify acoustic parameters to avoid acoustic masking by low-frequency city rumble. Specifically, species occupying louder habitats are predicted to shift their minimum vocal frequencies upward into higher spectral bands.",
    "Which choice best uses data from the table to support the ornithologists' hypothesis?",
    [
        "The House Sparrow, recorded at the highest ambient noise level (74 dB), exhibited the highest minimum song frequency (3,910 Hz), whereas the Song Sparrow had the lowest values for both metrics.",
        "The European Robin sang for a longer duration (2.1 s) than the Great Tit (1.4 s) despite experiencing lower ambient noise levels.",
        "The Great Tit had a lower minimum frequency than the House Sparrow despite experiencing identical urban traffic volumes.",
        "All four species exhibited identical minimum song frequencies regardless of variations in ambient city noise."
    ],
    "A",
    "Choice A is correct. The hypothesis states louder habitats correlate with higher minimum frequencies. Comparing the highest (House Sparrow: 74 dB / 3,910 Hz) and lowest (Song Sparrow: 65 dB / 2,410 Hz) directly supports this."
))

rw1.append(make_mcq(
    "t1-rw-m1-q12", DOMAINS["RW"]["INFO"], "Command of Evidence: Textual", "Medium",
    "In her study of 19th-century domestic economy manuals, historian Clara Vance argues that middle-class advice manuals did not simply mirror established domestic realities; rather, they constructed an idealized, prescriptive vision of domesticity intended to reassure families experiencing economic anxiety amidst volatile market panics.",
    "Which quotation from a 19th-century domestic manual would most directly support Vance's argument?",
    [
        "\"Though fortunes outside these parlor walls may crumble in the mercantile exchange overnight, within this sanctified hearth the orderly homemaker preserves an unchanging haven of serenity and moral virtue.\"",
        "\"The price of wholesale tallow and lard has risen fourteen percent across the northeastern rail depots this autumn.\"",
        "\"A good iron stove requires three hours of continuous stoking before the oven chamber reaches sufficient temperature for pastry.\"",
        "\"Most families in our township have hired domestic assistants to wash linens and tend the winter garden.\""
    ],
    "A",
    "Choice A is correct. It directly expresses an idealized moral haven created to alleviate anxiety about outside mercantile volatility, aligning with Vance's claim."
))

rw1.append(make_mcq(
    "t1-rw-m1-q13", DOMAINS["RW"]["INFO"], "Inferences", "Hard",
    "Under normal physiological conditions, mammalian skeletal muscles rely predominantly on oxidative phosphorylation for sustained low-intensity aerobic activity. When physical exertion escalates past the anaerobic threshold, cells ramp up glycolysis, producing pyruvate faster than mitochondria can process it, which leads to lactate accumulation. For decades, athletes believed lactate was merely a toxic metabolic waste product responsible for muscle fatigue. However, recent radiolabeling studies reveal that hepatocytes and cardiac myocytes absorb circulating lactate from bloodstream pathways and rapidly reconvert it into glucose or direct fuel. Thus, rather than being an inert fatigue agent, lactate _____.",
    "Which choice most logically completes the text?",
    [
        "serves as an adaptable, mobile energy shuttle that transfers carbohydrate fuel between differentiated tissues",
        "completely replaces adenosine triphosphate (ATP) as the exclusive chemical catalyst for muscular contraction",
        "prevents skeletal muscle cells from engaging in aerobic respiration during prolonged periods of rest",
        "causes irreversible mitochondrial damage whenever athletic exertion exceeds baseline resting levels"
    ],
    "A",
    "Choice A is correct. The text explains that liver and heart cells absorb lactate and use it as fuel or reconvert it to glucose, functioning as an energy shuttle."
))

rw1.append(make_mcq(
    "t1-rw-m1-q14", DOMAINS["RW"]["INFO"], "Central Ideas and Details", "Medium",
    "In classical physics, black holes were conceptualized as perfect gravitational sinks from which no radiation or matter could escape. In 1974, physicist Stephen Hawking applied quantum field theory to curved spacetime and revealed that quantum fluctuations near the event horizon generate virtual particle-antiparticle pairs. When one particle falls past the horizon and its counterpart escapes into space, the black hole loses mass, emitting what is now known as Hawking radiation. Over astronomical timescales, this implies that isolated black holes will eventually evaporate entirely.",
    "According to the text, what causes a black hole to emit Hawking radiation?",
    [
        "The escape of one particle from a quantum virtual pair generated near the event horizon while the other particle is captured.",
        "The sudden catastrophic collapse of dense baryonic matter into a macroscopic mathematical singularity.",
        "Thermonuclear fusion reactions igniting between cosmic gas clouds and interstellar magnetic fields.",
        "The absorption of superheated accretion disk plasma by neighboring galactic nuclei."
    ],
    "A",
    "Choice A is correct. Hawking radiation occurs when one particle from a quantum virtual pair near the horizon escapes into space while its partner is absorbed."
))

# 15-21 Standard English Conventions (Grammar)
rw1.append(make_mcq(
    "t1-rw-m1-q15", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "During the Renaissance, Venetian glassmakers on the island of Murano were forbidden to leave the republic without special _____ the city council feared foreign rivals would acquire their proprietary secret for crafting crystalline glass.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["dispensation, because", "dispensation; because", "dispensation, and", "dispensation because"],
    "A",
    "Choice A is correct. 'During the Renaissance... dispensation' is an independent clause, and 'because the city council feared...' is a subordinate explanatory clause. A comma followed by because cleanly connects them."
))

rw1.append(make_mcq(
    "t1-rw-m1-q16", DOMAINS["RW"]["CONV"], "Boundaries", "Medium",
    "The archaeological excavation uncovered hundreds of artifacts dating to the late Bronze Age: bronze sickles, ceramic storage vessels, woven textile fragments, and ornamental amber _____ all of which had remained preserved within the waterlogged peat bog.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["beads;", "beads,", "beads—", "beads:"],
    "B",
    "Choice B is correct. A comma followed by the nonessential relative clause 'all of which had remained preserved...' properly attaches the clause to the preceding noun list."
))

rw1.append(make_mcq(
    "t1-rw-m1-q17", DOMAINS["RW"]["CONV"], "Subject-Verb Agreement", "Easy",
    "A recent survey of tropical rainforest epiphytes found that the structural complexity of host tree canopies _____ directly correlated with the species richness of resident bryophyte communities.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["is", "are", "were", "have been"],
    "A",
    "Choice A is correct. The head noun of the subject is 'the structural complexity' (singular), which requires the singular verb 'is'."
))

rw1.append(make_mcq(
    "t1-rw-m1-q18", DOMAINS["RW"]["CONV"], "Modifiers", "Medium",
    "Having completed an exhaustive two-year survey of orbital trajectory data from the Hubble Space Telescope, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
        "astrophysicist Dr. Marcus Chen identified a subtle perturbation caused by a previously undocumented Kuiper Belt object.",
        "a subtle perturbation caused by a previously undocumented Kuiper Belt object was identified by astrophysicist Dr. Marcus Chen.",
        "the identification of a previously undocumented Kuiper Belt object was achieved by astrophysicist Dr. Marcus Chen.",
        "it was possible for astrophysicist Dr. Marcus Chen to identify a subtle perturbation in the Kuiper Belt."
    ],
    "A",
    "Choice A is correct. The introductory modifying phrase 'Having completed an exhaustive two-year survey...' must logically modify 'astrophysicist Dr. Marcus Chen'."
))

rw1.append(make_mcq(
    "t1-rw-m1-q19", DOMAINS["RW"]["CONV"], "Punctuation", "Easy",
    "Biochemist Jennifer Doudna and her colleagues demonstrated that the Cas9 enzyme functions as molecular _____ guided by custom RNA sequences to introduce precise double-stranded breaks in target DNA.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["scissors,", "scissors;", "scissors:", "scissors"],
    "D",
    "Choice D is correct. No punctuation should separate the noun 'scissors' from its essential restrictive participle phrase 'guided by custom RNA sequences'."
))

rw1.append(make_mcq(
    "t1-rw-m1-q20", DOMAINS["RW"]["CONV"], "Boundaries", "Easy",
    "While the North American gray wolf typically hunts in cooperative packs across vast territorial _____ solitary coyotes often forage near suburban margins, scavenging opportunistic food sources.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["ranges,", "ranges;", "ranges", "ranges:"],
    "A",
    "Choice A is correct. A comma is required to separate the introductory dependent clause ('While the North American gray wolf...') from the independent main clause."
))

rw1.append(make_mcq(
    "t1-rw-m1-q21", DOMAINS["RW"]["CONV"], "Pronouns", "Easy",
    "In her landmark critique of neoclassical economics, Elinor Ostrom challenged the assumption that common-pool resources must inevitably be depleted; she demonstrated that community-governed pastures and fisheries often manage _____ sustainability far more effectively than centralized state agencies.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    ["their", "its", "they're", "it's"],
    "A",
    "Choice A is correct. The antecedent is 'community-governed pastures and fisheries' (plural), requiring the plural possessive pronoun 'their'."
))

# 22-24 Transitions
rw1.append(make_mcq(
    "t1-rw-m1-q22", DOMAINS["RW"]["EXPR"], "Transitions", "Easy",
    "Early cartographers assumed that Greenland and Africa were comparable in land area because Mercator projection maps dramatically exaggerate geographic features located near the poles. _____, Africa encompasses approximately 30.3 million square kilometers, whereas Greenland measures only 2.16 million square kilometers, making Africa roughly fourteen times larger.",
    "Which choice completes the text with the most logical transition?",
    ["In reality,", "Furthermore,", "Consequently,", "Similarly,"],
    "A",
    "Choice A is correct. 'In reality,' introduces the factual reality that contradicts the mistaken assumption described in the opening sentence."
))

rw1.append(make_mcq(
    "t1-rw-m1-q23", DOMAINS["RW"]["EXPR"], "Transitions", "Medium",
    "Many ceramic glazes develop micro-fissures upon cooling if the glaze and clay body have differing thermal expansion coefficients. _____, master potters formulate custom frits that contract at precisely the same rate as the underlying porcelain during kiln firings.",
    "Which choice completes the text with the most logical transition?",
    ["To prevent this defect,", "In other words,", "By contrast,", "Nevertheless,"],
    "A",
    "Choice A is correct. Custom frits are formulated specifically to avoid the micro-fissuring problem stated in the first sentence."
))

rw1.append(make_mcq(
    "t1-rw-m1-q24", DOMAINS["RW"]["EXPR"], "Transitions", "Easy",
    "Proponents of urban vertical farming emphasize that indoor hydroponic towers use up to 95 percent less water than conventional outdoor cropland. _____, the high electricity demand required to power artificial LED illumination throughout the growth cycle remains a substantial environmental drawback.",
    "Which choice completes the text with the most logical transition?",
    ["However,", "Therefore,", "In addition,", "Specifically,"],
    "A",
    "Choice A is correct. 'However,' introduces a contrasting counterpoint (high energy consumption) to the initial benefit (water efficiency)."
))

# 25-27 Rhetorical Synthesis
rw1.append(make_mcq(
    "t1-rw-m1-q25", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "The James Webb Space Telescope (JWST) was launched in December 2021.",
        "It observes celestial objects primarily in the infrared spectrum.",
        "The Hubble Space Telescope observes primarily in optical and ultraviolet wavelengths.",
        "Infrared astronomy allows JWST to peer through dense interstellar dust clouds that obscure visible light.",
        "In 2022, JWST captured unprecedented images of the Carina Nebula's 'Cosmic Cliffs'."
    ]),
    "The student wants to contrast the observational capabilities of the JWST with those of the Hubble Space Telescope. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "While the Hubble Space Telescope observes primarily in optical and ultraviolet wavelengths, the JWST observes in the infrared spectrum, enabling it to penetrate dense interstellar dust clouds.",
        "Launched in December 2021, the JWST captured unprecedented images of the Carina Nebula's 'Cosmic Cliffs' using infrared instruments.",
        "Infrared astronomy allows instruments like the JWST to peer through cosmic dust clouds that would otherwise block optical observations.",
        "Both the Hubble Space Telescope and the JWST are space-based observatories designed to study distant celestial phenomena."
    ],
    "A",
    "Choice A is correct. It directly contrasts the spectral capabilities of both telescopes and explains the operational consequence of JWST's infrared sensors."
))

rw1.append(make_mcq(
    "t1-rw-m1-q26", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Aaron Douglas (1899–1979) was a prominent artist of the Harlem Renaissance.",
        "He synthesized elements of African art, Art Deco, and modernist abstraction.",
        "His signature aesthetic incorporated geometric silhouettes bathed in concentric circles of light.",
        "In 1934, he painted the celebrated mural series Aspects of Negro Life for the New York Public Library.",
        "The mural series illustrates African American history from freedom in Africa through the Great Migration."
    ]),
    "The student wants to emphasize the thematic subject of Douglas's mural series Aspects of Negro Life. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Painted in 1934, Aaron Douglas's mural series Aspects of Negro Life illustrates African American history spanning from life in Africa through the Great Migration.",
        "Aaron Douglas, an influential Harlem Renaissance artist, developed a style combining African art with geometric silhouettes and circles of light.",
        "In 1934, Douglas completed Aspects of Negro Life, a mural series for the New York Public Library that utilized Art Deco and modernist abstraction.",
        "Synthesizing elements of African art and modernism, Aaron Douglas created numerous celebrated works between 1899 and 1979."
    ],
    "A",
    "Choice A is correct. It directly states the thematic content of the mural series (African American history from Africa through the Great Migration)."
))

rw1.append(make_mcq(
    "t1-rw-m1-q27", DOMAINS["RW"]["EXPR"], "Rhetorical Synthesis", "Medium",
    make_bullet_notes([
        "Geothermal power plants harness heat from underground hydrothermal reservoirs to drive steam turbines.",
        "Dry steam plants pipe underground steam directly into turbines.",
        "Flash steam plants draw high-pressure hot water into surface tanks, causing it to flash into vapor.",
        "Binary cycle plants pass moderately hot geothermal fluid through a heat exchanger to boil a secondary working fluid with a lower boiling point.",
        "Binary cycle systems produce virtually zero atmospheric emissions because fluids circulate in a closed loop."
    ]),
    "The student wants to highlight an operational feature unique to binary cycle geothermal plants. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
        "Unlike dry and flash steam systems, binary cycle plants operate as closed loops that vaporize a secondary fluid with a low boiling point, resulting in virtually zero emissions.",
        "Geothermal power plants generate clean electrical energy by extracting subterranean heat to drive industrial steam turbines.",
        "Flash steam plants use surface depressurization tanks, whereas dry steam plants pipe hot reservoir steam directly into electrical turbines.",
        "Hydrothermal reservoirs provide the heat energy necessary to power dry steam, flash steam, and binary cycle power generation facilities."
    ],
    "A",
    "Choice A is correct. It specifies the unique operational characteristic of binary cycle plants (closed loop boiling a secondary fluid) and the resulting zero emissions."
))

print(f"Test 1 RW Module 1 ready: {len(rw1)} questions.")
