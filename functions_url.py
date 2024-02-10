from urllib.parse import urlparse
from sklearn.metrics import confusion_matrix, precision_score, recall_score, roc_curve, roc_auc_score
import pandas as pd
def extract_subdomain_count(url):
    parsed_url = urlparse(url)
    subdomains = parsed_url.hostname.split('.')
    # Si hay más de un subdominio, restamos 1 para excluir el dominio principal
    if len(subdomains) > 1:
        return len(subdomains) - 1
    else:
        return 0

def calculate_domain_length(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    # Calculamos la longitud del nombre de dominio
    domain_length = len(domain) if domain else 0
    return domain_length

def has_file_path(url):
    parsed_url = urlparse(url)
    # Verificamos si hay una ruta de archivo en el path de la URL
    if parsed_url.path:
        return 1
    else:
        return 0

def count_parameters(url):
    parsed_url = urlparse(url)
    # Contamos el número de parámetros en la URL
    params = parsed_url.query.split('&')
    return len(params)

def count_slashes(url):
    parsed_url = urlparse(url)
    # Contamos el número total de barras en la URL
    return url.count('/')

def identify_dots_positions(url):
    # Identificamos las posiciones de los puntos en la URL
    return [i for i, char in enumerate(url) if char == '.']

def detect_numbers(url):
    # Detectamos números en el subdominio y los nombres de URL
    numbers = [char for char in url if char.isdigit()]
    return len(numbers)

def analyze_hierarchy(url):
    # Analizamos la estructura jerárquica de la URL
    parsed_url = urlparse(url)
    hierarchy = parsed_url.path.split('/')
    return len(hierarchy)

def extract_domain_extension(url):
    parsed_url = urlparse(url)
    # Extraemos la extensión de dominio de la URL
    domain_parts = parsed_url.hostname.split('.')
    if len(domain_parts) > 1:
        return domain_parts[-1]
    else:
        return None

def check_uncommon_characters(url):
    # Verificamos la presencia de caracteres poco comunes en la URL
    uncommon_chars = set(url) - set('abcdefghijklmnopqrstuvwxyz0123456789.-/:?=&')
    return len(uncommon_chars) > 0

def check_hyphens_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    # Verificamos la presencia de guiones en el nombre de dominio
    return '-' in domain

def calculate_vowel_consonant_ratio(url):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    # Calculamos la proporción de vocales a consonantes en la URL
    vowel_count = sum(1 for char in url if char.lower() in vowels)
    consonant_count = sum(1 for char in url if char.lower() in consonants)
    return vowel_count / consonant_count if consonant_count != 0 else 0

def identify_special_characters(url):
    # Identificamos el uso de caracteres especiales en la URL
    special_chars = set(url) - set('abcdefghijklmnopqrstuvwxyz0123456789.-/:?=&')
    return len(special_chars)

def analyze_entropy(url):
    # Analizamos la entropía de los componentes de la URL
    components = urlparse(url)
    entropy = len(set(components)) / len(components)
    return entropy

def detect_url_patterns(url):
    # Detectamos patrones en secuencias de URL
    patterns = ['http', 'https', 'www']
    for pattern in patterns:
        if pattern in url:
            return 1
    return 0
# Definir una función para calcular y almacenar las métricas en un DataFrame
def calculate_metrics(y_true, y_pred, model_name):
    # Calcular la matriz de confusión
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    # Calcular la precisión
    precision = precision_score(y_true, y_pred)
    
    # Calcular el recall
    recall = recall_score(y_true, y_pred)
    
    # Calcular la puntuación AUC-ROC
    fpr, tpr, _ = roc_curve(y_true, y_pred)
    auc = roc_auc_score(y_true, y_pred)
    
    # Crear un DataFrame con las métricas
    metrics_df = pd.DataFrame({
        'Model': [model_name],
        'True Negative': [tn],
        'False Positive': [fp],
        'False Negative': [fn],
        'True Positive': [tp],
        'Precision': [precision],
        'Recall': [recall],
        'AUC-ROC': [auc]
    })
    
    return metrics_df
