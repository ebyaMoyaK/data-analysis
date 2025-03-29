# Mastocytosis Patient Survey: Symptoms, Triggers and Treatments

## Description

This dataset contains anonymized information on patients with mastocytosis, a rare disease characterized by an abnormal accumulation of mast cells in various tissues.

## Content

This package contains the following files:

* `mastocytosis_patient_survey.csv`: The primary dataset with all information.
* `symptom_triggers_analysis.csv`: Analysis of individual symptom triggers.
* `clinical_symptoms_analysis.csv`: Analysis of individual symptoms.
* `treatment_modalities_analysis.csv`: Analysis of individual treatments.

## Dataset Structure

The primary dataset contains information from 50 participants and includes the following columns:

* `Participant_ID`
* `Age`
* `Gender`
* `Country`
* `Mastocytosis_Diagnosis_Status`
* `Mastocytosis_Type`
* `Primary_Symptoms`
* `Symptom_Frequency`
* `Anaphylactic_Reaction_History`
* `Symptom_Triggers`
* `Current_Treatments`
* `Hospitalization_History`
* `Quality_of_Life_Impact_Score`
* `Specialist_Consultation_Status`

## Multiple Value Columns

Three columns in the dataset contain multiple values separated by commas:

1. **Symptom_Triggers**: Symptom triggers for each patient
2. **Primary_Symptoms**: Main symptoms reported by each patient
3. **Current_Treatments**: Treatments currently followed by each patient

To facilitate analysis, we have extracted these individual values into separate files that show the frequency of each element in the study population.

## Key Findings

### Most Frequent Triggers

```
1. Stress: 15 patients (30.0%)
2. Heat: 9 patients (18.0%)
3. Food: 8 patients (16.0%)
4. Alcohol: 7 patients (14.0%)
5. Temperature changes: 5 patients (10.0%)
6. Friction: 3 patients (6.0%)
7. Medications: 2 patients (4.0%)
8. Pineapple: 2 patients (4.0%)
9. Fatigue: 2 patients (4.0%)
10. Harsh chemicals: 2 patients (4.0%)
```

### Most Frequent Symptoms

```
1. Itching: 34 patients (68.0%)
2. Chronic fatigue: 31 patients (62.0%)
3. Digestive issues: 28 patients (56.0%)
4. Flushing: 23 patients (46.0%)
5. Bone pain: 20 patients (40.0%)
6. Anxiety: 3 patients (6.0%)
7. Brain fog: 3 patients (6.0%)
8. Allergies: 2 patients (4.0%)
9. Skin lesions: 2 patients (4.0%)
10. Headaches: 2 patients (4.0%)
```

### Most Frequent Treatments

```
1. Antihistamines: 28 patients (56.0%)
2. Corticosteroids: 2 patients (4.0%)
3. Quercetin: 2 patients (4.0%)
4. Omalizumab (Xolair): 2 patients (4.0%)
5. Cromolyn sodium: 2 patients (4.0%)
6. Pain management medications: 1 patient (2.0%)
7. Diamine Oxidase: 1 patient (2.0%)
8. Topical estradiol/estriol with progesterone: 1 patient (2.0%)
9. Mast cell stabilizers: 1 patient (2.0%)
10. Prednisolone: 1 patient (2.0%)
```

## Usage

This dataset can be used for:

* Analyzing common symptoms of mastocytosis
* Studying the most frequent triggers
* Examining current therapeutic approaches
* Exploring correlations between types of mastocytosis and symptoms
* Investigating quality of life impact based on disease characteristics

## Anonymization Note

All data has been anonymized to protect participant privacy. Unique identifiers (Participant_ID) have been randomly assigned and do not correspond to any information that could identify patients.