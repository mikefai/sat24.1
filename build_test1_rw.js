// Generator for Digital SAT Practice Test 1
import fs from 'fs';
import {
  makeVocabQuestion, makeStructureQuestion, makeDualPassageQuestion,
  makeCentralIdeaQuestion, makeInferenceQuestion, makeQuantitativeEvidenceQuestion,
  makeTextualEvidenceQuestion, makeGrammarQuestion, makeTransitionQuestion,
  makeRhetoricalSynthesisQuestion
} from './src/data/builder_rw.js';
import {
  makeMathMCQ, makeMathSPR, svgRightTriangle, svgCircleWithAngle, svgCoordinateParabola
} from './src/data/builder_math.js';
import { DOMAINS } from './src/data/scoring.js';

console.log("Generating Test 1: 108 questions (54 RW, 54 Math)...");

// ==========================================
// TEST 1 - READING & WRITING MODULE 1 (27 Qs)
// ==========================================
const rw_m1 = [
  // 1-5 Words in Context
  makeVocabQuestion(
    "t1-rw-m1-q1",
    "In her 2021 monograph on architectural history, Dr. Elena Rostova argues that the sudden adoption of reinforced concrete in urban civic centers was neither accidental nor _____; rather, it represented a calculated response to rising industrial fire hazards and municipal insurance mandates.",
    "_____",
    ["capricious", "inevitable", "pragmatic", "laudable"],
    "A",
    "Choice A is correct. 'Capricious' means impulsive, unpredictable, or determined by chance. The sentence states that the adoption was 'neither accidental nor [capricious]; rather, it represented a calculated response'. This sets up a contrast with 'calculated'.",
    "Easy"
  ),
  makeVocabQuestion(
    "t1-rw-m1-q2",
    "Although the ancient library catalog contained numerous gaps and obscure references, the archivist was able to _____ the provenance of the 14th-century illuminated manuscript by correlating watermarks in the rag paper with regional guild registries.",
    "_____",
    ["substantiate", "repudiate", "obfuscate", "disseminate"],
    "A",
    "Choice A is correct. 'Substantiate' means to establish or prove with evidence. Correlating watermarks with registries allowed the archivist to verify/prove the manuscript's origins.",
    "Medium"
  ),
  makeVocabQuestion(
    "t1-rw-m1-q3",
    "The ecologist noted that while apex predators often exert a _____ influence across trophic cascades, their absence does not merely diminish local biodiversity; it fundamentally restructures the physical geomorphology of riverbanks by releasing herbivore populations from foraging pressure.",
    "_____",
    ["pervasive", "peripheral", "transitory", "redundant"],
    "A",
    "Choice A is correct. 'Pervasive' means widespread or having an effect throughout an entire system. The context describes apex predators reshaping entire food webs and geomorphology, demonstrating a pervasive influence.",
    "Medium"
  ),
  makeVocabQuestion(
    "t1-rw-m1-q4",
    "In public interviews, the minimalist composer was notoriously _____, often replying to expansive inquiries regarding his symphonic motifs with mere single-syllable acknowledgments or prolonged silences.",
    "_____",
    ["laconic", "loquacious", "effusive", "bellicose"],
    "A",
    "Choice A is correct. 'Laconic' means concise or using very few words. Answering with single-syllable words and silence directly matches this definition.",
    "Hard"
  ),
  makeVocabQuestion(
    "t1-rw-m1-q5",
    "Unlike the flamboyant, highly ornamented facades characteristic of Baroque architecture, the civic municipal hall displays a rigorous aesthetic _____, relying exclusively on unadorned limestone blocks and geometric symmetry to project authority.",
    "_____",
    ["austerity", "ebullience", "incongruity", "opulence"],
    "A",
    "Choice A is correct. 'Austerity' refers to severe simplicity or plainness. Relying on unadorned stone and symmetry in contrast to flamboyant ornamentation illustrates austerity.",
    "Medium"
  ),

  // 6-8 Text Structure & Purpose / Dual Passages
  makeStructureQuestion(
    "t1-rw-m1-q6",
    "For decades, paleobotanists assumed that angiosperms (flowering plants) diversified rapidly during the mid-Cretaceous period in what Charles Darwin famously termed an 'abominable mystery.' However, recent molecular clock analyses calibrated with fossil spores from the Early Jurassic suggest that the lineage had already diverged tens of millions of years earlier than macroscopic macrofossils indicate. <u>These findings do not dispute the explosion of ecological forms in the Cretaceous, but rather recalibrate the evolutionary tempo, suggesting a prolonged cryptic phase of evolutionary experimentation.</u>",
    "Which choice best describes the function of the underlined sentence in the text as a whole?",
    [
      "It clarifies the precise nature of the challenge posed by recent molecular clock findings to established historical models.",
      "It dismisses molecular clock analysis as fundamentally incompatible with the physical macrofossil record.",
      "It introduces a third competing hypothesis regarding the geographic origins of Jurassic flowering plants.",
      "It summarizes Charles Darwin's original conceptualization of Cretaceous floral diversification."
    ],
    "A",
    "Choice A is correct. The underlined sentence specifies that the new findings don't completely overturn the Cretaceous explosion, but rather explain that it was preceded by a long cryptic phase, clarifying how the new data impacts existing models.",
    "Medium"
  ),
  makeDualPassageQuestion(
    "t1-rw-m1-q7",
    "In a 2018 paper, economist David Miller argued that automated inventory management algorithms universally suppress inflationary price volatility by instantly matching wholesale supply orders with real-time consumer checkout demand across national retail chains.",
    "Sociologist Priya Nair examined rural grocery cooperatives and observed that algorithm-driven supply chains frequently trigger localized phantom shortages when regional freight disruptions decouple local demand signals from centralized warehouse dispatch algorithms.",
    "Based on the texts, how would Nair (Text 2) most likely respond to Miller's assertion in Text 1?",
    [
      "By asserting that Miller overlooks how supply chain disruptions can cause automated systems to produce localized distribution failures.",
      "By arguing that rural retail cooperatives deliberately disable pricing algorithms during national economic recessions.",
      "By agreeing that real-time checkout monitoring eliminates consumer demand spikes in major metropolitan areas.",
      "By demonstrating that automated wholesale ordering is significantly more expensive than manual ledger tracking."
    ],
    "A",
    "Choice A is correct. While Miller claims automated algorithms universally suppress volatility, Nair points out that regional freight disruptions cause the algorithms to produce 'localized phantom shortages', showing that Miller's claim is an overgeneralization.",
    "Hard"
  ),
  makeStructureQuestion(
    "t1-rw-m1-q8",
    "Virginia Woolf's 1925 novel <i>Mrs. Dalloway</i> famously eschews conventional chronological plotting in favor of free indirect discourse, immersing readers within the uninterrupted cognitive flow of its characters over the span of a single London day. Through this structural choice, Woolf achieves a dual representation: the external, mechanized chime of Big Ben punctuating objective time, juxtaposed against the fluid, elastic interiority of human memory and psychological perception.",
    "Which choice best states the primary purpose of the text?",
    [
      "To analyze how Woolf uses narrative technique to contrast objective chronological time with subjective mental experience.",
      "To criticize the lack of traditional plot structure and chronological coherence in early 20th-century British fiction.",
      "To trace the autobiographical origins of Virginia Woolf's thematic interest in London's civic infrastructure.",
      "To compare the commercial reception of <i>Mrs. Dalloway</i> with that of other modernist novels published in 1925."
    ],
    "A",
    "Choice A is correct. The text explicitly highlights how Woolf's structural choice juxtaposes 'objective time' (Big Ben) against 'the fluid, elastic interiority of human memory'.",
    "Medium"
  ),

  // 9-13 Central Ideas, Inferences & Evidence
  makeCentralIdeaQuestion(
    "t1-rw-m1-q9",
    "In deep-sea hydrothermal vents, where sunlight cannot penetrate, entire biological communities thrive independently of solar energy. Instead of relying on plant-based photosynthesis, these ecosystems are anchored by chemotrophic bacteria that oxidize hydrogen sulfide dissolved in the superheated, mineral-rich effluent emitted from the seafloor crust. Tubeworms, clams, and vent shrimp harbor these bacteria endosymbiotically or graze upon bacterial mats, demonstrating that complex multicellular life can be sustained entirely through geothermal and geochemical inputs.",
    "Which choice best summarizes the central idea of the text?",
    [
      "Hydrothermal vent ecosystems are powered by chemotrophic bacteria that convert geothermal chemical compounds into organic energy.",
      "Sunlight-dependent marine organisms have gradually migrated to benthic hydrothermal fissures to escape surface predators.",
      "Tubeworms and vent shrimp produce hydrogen sulfide to generate protective thermal barriers against abyssal freezing temperatures.",
      "Photosynthesis remains an indispensable indirect biological process for all organisms residing in oceanic benthic zones."
    ],
    "A",
    "Choice A is correct. The passage explains that instead of solar photosynthesis, vent communities are fueled by chemotrophic bacteria oxidizing hydrogen sulfide emitted from geothermal vents.",
    "Easy"
  ),
  makeInferenceQuestion(
    "t1-rw-m1-q10",
    "Biologists studying monarch butterfly migration have long known that the insects navigate using a time-compensated sun compass, which integrates the sun's azimuth with internal circadian clocks in their antennae. In a controlled experiment, researchers placed migrating monarchs in a planetarium where magnetic fields could be artificially reversed while celestial lighting remained constant. The butterflies maintained their south-southwest trajectory regardless of magnetic disorientation; however, when the researchers shifted the artificial light-dark schedule by six hours, the butterflies' flight headings rotated by roughly 90 degrees. This finding strongly suggests that _____.",
    "Which choice most logically completes the text?",
    [
      "monarch butterflies prioritize solar and circadian cues over geomagnetic orientation during migratory navigation",
      "geomagnetic field lines serve as the exclusive sensory mechanism guiding monarchs across continental distances",
      "circadian clock proteins in antennae operate completely independently of external diurnal photoperiods",
      "monarchs rely primarily on geographic landmarks such as coastlines rather than astronomical orientation"
    ],
    "A",
    "Choice A is correct. Reversing the magnetic field had no effect on trajectory, but shifting the light-dark schedule altered heading by 90 degrees, proving solar/circadian cues take priority over geomagnetic ones.",
    "Medium"
  ),
  makeQuantitativeEvidenceQuestion(
    "t1-rw-m1-q11",
    `<table style="width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 13px;">
      <thead>
        <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
          <th style="padding: 6px; text-align: left;">Bird Species</th>
          <th style="padding: 6px; text-align: center;">Urban Ambient Noise (dB)</th>
          <th style="padding: 6px; text-align: center;">Song Min Freq (Hz)</th>
          <th style="padding: 6px; text-align: center;">Song Duration (s)</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 5px;">European Robin</td><td style="padding: 5px; text-align: center;">68</td><td style="padding: 5px; text-align: center;">2,850</td><td style="padding: 5px; text-align: center;">2.1</td></tr>
        <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 5px;">Great Tit</td><td style="padding: 5px; text-align: center;">71</td><td style="padding: 5px; text-align: center;">3,420</td><td style="padding: 5px; text-align: center;">1.4</td></tr>
        <tr style="border-bottom: 1px solid #e2e8f0;"><td style="padding: 5px;">House Sparrow</td><td style="padding: 5px; text-align: center;">74</td><td style="padding: 5px; text-align: center;">3,910</td><td style="padding: 5px; text-align: center;">0.9</td></tr>
        <tr><td style="padding: 5px;">Song Sparrow</td><td style="padding: 5px; text-align: center;">65</td><td style="padding: 5px; text-align: center;">2,410</td><td style="padding: 5px; text-align: center;">2.8</td></tr>
      </tbody>
    </table>`,
    "Ornithologists hypothesize that urban songbirds modify acoustic parameters to avoid acoustic masking by low-frequency anthropogenic city rumble. Specifically, species occupying louder urban habitats are predicted to shift their minimum vocal frequencies upward into higher spectral bands.",
    "Which choice best uses data from the table to support the ornithologists' hypothesis?",
    [
      "The House Sparrow, recorded at the highest ambient noise level (74 dB), exhibited the highest minimum song frequency (3,910 Hz), whereas the Song Sparrow had the lowest values for both metrics.",
      "The European Robin sang for a longer duration (2.1 s) than the Great Tit (1.4 s) despite experiencing lower ambient noise levels.",
      "The Great Tit had a lower minimum frequency than the House Sparrow despite experiencing identical urban traffic volumes.",
      "All four species exhibited identical minimum song frequencies regardless of variations in ambient city noise."
    ],
    "A",
    "Choice A is correct. The hypothesis states that louder habitats correspond to higher minimum vocal frequencies. Showing that the loudest environment (House Sparrow at 74 dB) had the highest frequency (3,910 Hz) and lowest (Song Sparrow at 65 dB / 2,410 Hz) directly supports the hypothesis.",
    "Medium"
  ),
  makeTextualEvidenceQuestion(
    "t1-rw-m1-q12",
    "In her study of 19th-century domestic economy manuals, historian Clara Vance argues that middle-class advice manuals did not simply mirror established domestic realities; rather, they constructed an idealized, prescriptive vision of domesticity intended to reassure families experiencing economic anxiety amidst volatile market panics.",
    "Which quotation from a 19th-century domestic manual would most directly support Vance's argument?",
    [
      "\"Though fortunes outside these parlor walls may crumble in the mercantile exchange overnight, within this sanctified hearth the orderly homemaker preserves an unchanging haven of serenity and moral virtue.\"",
      "\"The price of wholesale tallow and lard has risen fourteen percent across the northeastern rail depots this autumn.\"",
      "\"A good iron stove requires three hours of continuous stoking before the oven chamber reaches sufficient temperature for pastry.\"",
      "\"Most families in our township have hired domestic assistants to wash linens and tend the winter garden.\""
    ],
    "A",
    "Choice A is correct. It directly expresses an idealized refuge ('unchanging haven') designed to counteract economic volatility ('fortunes outside these parlor walls may crumble in the mercantile exchange'), supporting Vance's claim.",
    "Medium"
  ),
  makeInferenceQuestion(
    "t1-rw-m1-q13",
    "Under normal physiological conditions, mammalian skeletal muscles rely predominantly on oxidative phosphorylation for sustained low-intensity aerobic activity. When physical exertion escalates past the anaerobic threshold, cells ramp up glycolysis, producing pyruvate faster than mitochondria can process it, which leads to lactate accumulation. For decades, athletes believed lactate was merely a toxic metabolic waste product responsible for muscle fatigue. However, recent radiolabeling studies reveal that hepatocytes and cardiac myocytes absorb circulating lactate from bloodstream pathways and rapidly reconvert it into glucose or direct fuel. Thus, rather than being an inert fatigue agent, lactate _____.",
    "Which choice most logically completes the text?",
    [
      "serves as an adaptable, mobile energy shuttle that transfers carbohydrate fuel between differentiated tissues",
      "completely replaces adenosine triphosphate (ATP) as the exclusive chemical catalyst for muscular contraction",
      "prevents skeletal muscle cells from engaging in aerobic respiration during prolonged periods of rest",
      "causes irreversible mitochondrial damage whenever athletic exertion exceeds baseline resting levels"
    ],
    "A",
    "Choice A is correct. The passage shows that other tissues (liver, heart) absorb lactate from the blood and use it as fuel or turn it into glucose, demonstrating it functions as an energy shuttle.",
    "Hard"
  ),

  // 14-20 Standard English Conventions (Grammar)
  makeGrammarQuestion(
    "t1-rw-m1-q14",
    "During the Renaissance, Venetian glassmakers on the island of Murano were forbidden to leave the republic without special _____ the city council feared foreign rivals would acquire their proprietary secret for crafting crystalline glass.",
    null,
    [
      "dispensation, because",
      "dispensation; because",
      "dispensation, and",
      "dispensation because"
    ],
    "A",
    "Choice A is correct. 'During the Renaissance... special dispensation' is an independent clause, and 'because the city council feared...' is a subordinate explanatory clause. A comma followed by because properly connects them without creating a run-on or unnecessary punctuation.",
    "Medium"
  ),
  makeGrammarQuestion(
    "t1-rw-m1-q15",
    "The archaeological excavation uncovered hundreds of artifacts dating to the late Bronze Age: bronze sickles, ceramic storage vessels, woven textile fragments, and ornamental amber _____ all of which had remained preserved within the waterlogged peat bog.",
    null,
    [
      "beads;",
      "beads,",
      "beads—",
      "beads:"
    ],
    "B",
    "Choice B is correct. A comma followed by the relative pronoun phrase 'all of which had remained preserved...' correctly modifies the preceding list of artifacts in a nonessential relative clause.",
    "Medium"
  ),
  makeGrammarQuestion(
    "t1-rw-m1-q16",
    "A recent survey of tropical rainforest epiphytes found that the structural complexity of host tree canopies _____ directly correlated with the species richness of resident bryophyte communities.",
    null,
    [
      "is",
      "are",
      "were",
      "have been"
    ],
    "A",
    "Choice A is correct. The grammatical subject is 'the structural complexity' (singular), which requires the singular present verb 'is'. 'Of host tree canopies' is an intervening prepositional phrase.",
    "Easy"
  ),
  makeGrammarQuestion(
    "t1-rw-m1-q17",
    "Having completed an exhaustive two-year survey of orbital trajectory data from the Hubble Space Telescope, _____.",
    "Which choice completes the text so that it conforms to the conventions of Standard English?",
    [
      "astrophysicist Dr. Marcus Chen identified a subtle perturbation caused by a previously undocumented Kuiper Belt object.",
      "a subtle perturbation caused by a previously undocumented Kuiper Belt object was identified by astrophysicist Dr. Marcus Chen.",
      "the identification of a previously undocumented Kuiper Belt object was achieved by astrophysicist Dr. Marcus Chen.",
      "it was possible for astrophysicist Dr. Marcus Chen to identify a subtle perturbation in the Kuiper Belt."
    ],
    "A",
    "Choice A is correct. The introductory participial phrase 'Having completed an exhaustive two-year survey...' must logically modify the subject that follows immediately: 'astrophysicist Dr. Marcus Chen'. In B, C, and D, the modifier dangles.",
    "Medium"
  ),
  makeGrammarQuestion(
    "t1-rw-m1-q18",
    "Biochemist Jennifer Doudna and her colleagues demonstrated that the Cas9 enzyme functions as molecular _____ guided by custom RNA sequences to introduce precise double-stranded breaks in target DNA.",
    null,
    [
      "scissors,",
      "scissors;",
      "scissors:",
      "scissors"
    ],
    "D",
    "Choice D is correct. No punctuation should interrupt the noun phrase 'molecular scissors' and its essential participial modifier 'guided by custom RNA sequences'.",
    "Easy"
  ),
  makeGrammarQuestion(
    "t1-rw-m1-q19",
    "While the North American gray wolf typically hunts in cooperative packs across vast territorial _____ solitary coyotes often forage near suburban margins, scavenging opportunistic food sources.",
    null,
    [
      "ranges,",
      "ranges;",
      "ranges",
      "ranges:"
    ],
    "A",
    "Choice A is correct. The sentence begins with a dependent adverbial clause 'While the North American gray wolf...', which requires a comma before the main independent clause ('solitary coyotes often forage...').",
    "Easy"
  ),
  makeGrammarQuestion(
    "t1-rw-m1-q20",
    "In her landmark critique of neoclassical economics, Elinor Ostrom challenged the assumption that common-pool resources must inevitably be depleted; she demonstrated that community-governed pastures and fisheries often manage _____ sustainability far more effectively than centralized state agencies.",
    null,
    [
      "their",
      "its",
      "they're",
      "it's"
    ],
    "A",
    "Choice A is correct. The possessive pronoun refers to 'community-governed pastures and fisheries' (plural), so 'their' is correct.",
    "Easy"
  ),

  // 21-23 Transitions
  makeTransitionQuestion(
    "t1-rw-m1-q21",
    "Early cartographers assumed that Greenland and Africa were comparable in land area because Mercator projection maps dramatically exaggerate geographic features located near the poles. _____, Africa encompasses approximately 30.3 million square kilometers, whereas Greenland measures only 2.16 million square kilometers, making Africa roughly fourteen times larger.",
    ["In reality,", "Furthermore,", "Consequently,", "Similarly,"],
    "A",
    "Choice A is correct. 'In reality,' introduces the factual correction to the erroneous assumption described in the first sentence.",
    "Easy"
  ),
  makeTransitionQuestion(
    "t1-rw-m1-q22",
    "Many ceramic glazes develop micro-fissures upon cooling if the glaze and clay body have differing thermal expansion coefficients. _____, master potters formulate custom frits that contract at precisely the same rate as the underlying porcelain during kiln firings.",
    ["To prevent this defect,", "In other words,", "By contrast,", "Nevertheless,"],
    "A",
    "Choice A is correct. Formulating custom frits is a deliberate action taken to prevent the micro-fissuring problem described in the previous sentence.",
    "Medium"
  ),
  makeTransitionQuestion(
    "t1-rw-m1-q23",
    "Proponents of urban vertical farming emphasize that indoor hydroponic towers use up to 95 percent less water than conventional outdoor cropland. _____, the high electricity demand required to power artificial LED illumination throughout the growth cycle remains a substantial environmental drawback.",
    ["However,", "Therefore,", "In addition,", "Specifically,"],
    "A",
    "Choice A is correct. 'However,' introduces a contrasting counterpoint (high energy consumption) to the initial benefit (drastically reduced water use).",
    "Easy"
  ),

  // 24-27 Rhetorical Synthesis
  makeRhetoricalSynthesisQuestion(
    "t1-rw-m1-q24",
    [
      "The James Webb Space Telescope (JWST) was launched in December 2021.",
      "It observes celestial objects primarily in the infrared spectrum.",
      "The Hubble Space Telescope observes primarily in optical and ultraviolet wavelengths.",
      "Infrared astronomy allows JWST to peer through dense interstellar dust clouds that obscure visible light.",
      "In 2022, JWST captured unprecedented images of the Carina Nebula's 'Cosmic Cliffs'."
    ],
    "The student wants to contrast the observational capabilities of the JWST with those of the Hubble Space Telescope. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
      "While the Hubble Space Telescope observes primarily in optical and ultraviolet wavelengths, the JWST observes in the infrared spectrum, enabling it to penetrate dense interstellar dust clouds.",
      "Launched in December 2021, the JWST captured unprecedented images of the Carina Nebula's 'Cosmic Cliffs' using infrared instruments.",
      "Infrared astronomy allows instruments like the JWST to peer through cosmic dust clouds that would otherwise block optical observations.",
      "Both the Hubble Space Telescope and the JWST are space-based observatories designed to study distant celestial phenomena."
    ],
    "A",
    "Choice A is correct. It directly contrasts the observational wavelengths of Hubble (optical/UV) and JWST (infrared) and explains the practical capability difference (penetrating dust clouds).",
    "Medium"
  ),
  makeRhetoricalSynthesisQuestion(
    "t1-rw-m1-q25",
    [
      "Aaron Douglas (1899–1979) was a prominent artist of the Harlem Renaissance.",
      "He synthesized elements of African art, Art Deco, and modernist abstraction.",
      "His signature aesthetic incorporated geometric silhouettes bathed in concentric circles of light.",
      "In 1934, he painted the celebrated mural series <i>Aspects of Negro Life</i> for the New York Public Library.",
      "The mural series illustrates African American history from freedom in Africa through the Great Migration."
    ],
    "The student wants to emphasize the thematic subject of Douglas's mural series <i>Aspects of Negro Life</i>. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
      "Painted in 1934, Aaron Douglas's mural series <i>Aspects of Negro Life</i> illustrates African American history spanning from life in Africa through the Great Migration.",
      "Aaron Douglas, an influential Harlem Renaissance artist, developed a style combining African art with geometric silhouettes and circles of light.",
      "In 1934, Douglas completed <i>Aspects of Negro Life</i>, a mural series for the New York Public Library that utilized Art Deco and modernist abstraction.",
      "Synthesizing elements of African art and modernism, Aaron Douglas created numerous celebrated works between 1899 and 1979."
    ],
    "A",
    "Choice A is correct. The goal is to emphasize the thematic subject of the mural series, which choice A explicitly does ('illustrates African American history spanning from life in Africa through the Great Migration').",
    "Medium"
  ),
  makeRhetoricalSynthesisQuestion(
    "t1-rw-m1-q26",
    [
      "Mycorrhizal fungi form mutualistic underground networks with plant roots.",
      "The fungi absorb soil water and phosphorus, delivering them directly to host plants.",
      "In exchange, host plants transfer photosynthetic carbohydrates to the fungal network.",
      "Recent research indicates that these fungal hyphae also transmit biochemical defense signals between neighboring trees during insect attacks."
    ],
    "The student wants to introduce the mutualistic resource exchange between mycorrhizal fungi and plants to an audience unfamiliar with the concept. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
      "Through underground mycorrhizal networks, fungi supply host plants with soil water and phosphorus in direct exchange for photosynthetic carbohydrates.",
      "In addition to exchanging nutrients, mycorrhizal networks can transmit warning signals between neighboring trees during insect infestations.",
      "Mycorrhizal fungi are subterranean organisms composed of fine threadlike structures known as hyphae that connect to tree roots.",
      "Plants rely on underground fungal networks to survive in phosphorus-deficient soils throughout temperate forests."
    ],
    "A",
    "Choice A is correct. It clearly introduces the two-way mutualistic exchange: fungi providing water/phosphorus and plants providing carbohydrates.",
    "Easy"
  ),
  makeRhetoricalSynthesisQuestion(
    "t1-rw-m1-q27",
    [
      "Geothermal power plants harness heat from underground hydrothermal reservoirs to drive steam turbines.",
      "Dry steam plants pipe underground steam directly into turbines.",
      "Flash steam plants draw high-pressure hot water into surface tanks, causing it to flash into vapor.",
      "Binary cycle plants pass moderately hot geothermal fluid through a heat exchanger to boil a secondary working fluid with a lower boiling point.",
      "Binary cycle systems produce virtually zero atmospheric emissions because fluids circulate in a closed loop."
    ],
    "The student wants to highlight an operational feature unique to binary cycle geothermal plants. Which choice most effectively uses the relevant information from the notes to accomplish this goal?",
    [
      "Unlike dry and flash steam systems, binary cycle plants operate as closed loops that vaporize a secondary fluid with a low boiling point, resulting in virtually zero emissions.",
      "Geothermal power plants generate clean electrical energy by extracting subterranean heat to drive industrial steam turbines.",
      "Flash steam plants use surface depressurization tanks, whereas dry steam plants pipe hot reservoir steam directly into electrical turbines.",
      "Hydrothermal reservoirs provide the heat energy necessary to power dry steam, flash steam, and binary cycle power generation facilities."
    ],
    "A",
    "Choice A is correct. It isolates the distinct operational feature of binary cycle plants (closed loop vaporizing a secondary working fluid with zero emissions) compared to dry and flash steam.",
    "Medium"
  )
];

console.log(`Test 1 RW Module 1 generated: ${rw_m1.length} questions`);
