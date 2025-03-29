"""
Data processing utilities for mastocytosis patient data.
"""

import pandas as pd
from collections import Counter
import os


def read_dataset(file_path, detect_separator=True):
    """
    Reads a dataset with automatic separator detection.
    
    Args:
        file_path (str): Path to the CSV file
        detect_separator (bool): Whether to try multiple separators
        
    Returns:
        pandas.DataFrame: The loaded dataset
    """
    if not detect_separator:
        return pd.read_csv(file_path)
        
    # Try different separators
    separators = [';', ',']
    for sep in separators:
        try:
            df = pd.read_csv(file_path, sep=sep)
            return df
        except:
            continue
    
    # If specific separators fail, try auto-detection
    try:
        df = pd.read_csv(file_path, sep=None, engine='python')
        return df
    except Exception as e:
        raise ValueError(f"Failed to read {file_path}: {str(e)}")


def normalize_column_values(column_name):
    """
    Get normalization mapping for a specific column.
    
    Args:
        column_name (str): Name of the column to normalize
        
    Returns:
        dict: Mapping of raw values to normalized values
    """
    # Normalization mappings for different columns
    mapping_dict = {
        'Symptom_Triggers': {
            'stress': 'Stress',
            'heat': 'Heat',
            'alcohol': 'Alcohol',
            'food': 'Food',
            'temperature changes': 'Temperature changes',
            'temperature change': 'Temperature changes',
            'temperature fluctuations': 'Temperature changes',
        },
        'Primary_Symptoms': {
            'itching': 'Itching',
            'flushing': 'Flushing',
            'chronic fatigue': 'Chronic fatigue', 
            'digestive issues': 'Digestive issues',
            'bone pain': 'Bone pain',
            'digestive issues (diarrhea, nausea...)': 'Digestive issues',
            'digestive issues (diarrhea, nausea)': 'Digestive issues',
        },
        'Current_Treatments': {
            'antihistamine': 'Antihistamines',
            'antihistamines': 'Antihistamines',
            'corticosteroid': 'Corticosteroids',
            'corticosteroids': 'Corticosteroids',
        }
    }
    
    return mapping_dict.get(column_name, {})


def extract_individual_items(df, column_name):
    """
    Extract and count individual elements from a column with multiple values.
    
    Args:
        df (pandas.DataFrame): Dataset containing the column
        column_name (str): Name of column with comma-separated values
        
    Returns:
        pandas.DataFrame: DataFrame with items and their frequencies
    """
    all_items = []
    mapping = normalize_column_values(column_name)
    
    for items_str in df[column_name]:
        if pd.notna(items_str) and items_str != 'N/A':
            
            items = [item.strip() for item in str(items_str).split(',')]
            
            
            normalized_items = []
            for item in items:
                
                if item.lower() in mapping:
                    normalized_items.append(mapping[item.lower()])
                else:
                    # Check if item starts with a mapping key
                    matched = False
                    for key, value in mapping.items():
                        if item.lower().startswith(key):
                            normalized_items.append(value)
                            matched = True
                            break
                    
                    # If no mapping found, capitalize first character
                    if not matched:
                        normalized_items.append(item[0].upper() + item[1:] if len(item) > 1 else item.upper())
            
            all_items.extend(normalized_items)
    
    # Count occurrences and create DataFrame
    item_counts = Counter(all_items)
    items_df = pd.DataFrame({
        'Item': list(item_counts.keys()),
        'Count': list(item_counts.values()),
        'Percentage': [round(count/len(df)*100, 1) for count in item_counts.values()]
    })
    
    return items_df.sort_values('Count', ascending=False)


def process_mastocytosis_data(input_file, output_dir='.'):
    """
    Process mastocytosis dataset and generate analysis files.
    
    Args:
        input_file (str): Path to input CSV file
        output_dir (str): Directory for output files
        
    Returns:
        dict: Dictionary with paths to generated files
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read dataset
    df = read_dataset(input_file)
    
    # Define output files
    output_files = {
        'Symptom_Triggers': os.path.join(output_dir, 'symptom_triggers_analysis.csv'),
        'Primary_Symptoms': os.path.join(output_dir, 'clinical_symptoms_analysis.csv'),
        'Current_Treatments': os.path.join(output_dir, 'treatment_modalities_analysis.csv')
    }
    
    # Process each column and save results
    results = {}
    for column, output_file in output_files.items():
        analysis_df = extract_individual_items(df, column)
        analysis_df.to_csv(output_file, index=False)
        results[column] = output_file
    
    return results