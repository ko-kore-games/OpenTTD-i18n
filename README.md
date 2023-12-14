
## Workflow for a new translation
1. txt_to_yaml.py
1. (translate strings in the yaml file)
1. (optional) postprocess_ko_Kore.py
1. yaml_to_txt.py

# Workflow for updating an existing translation
1. txt_to_yaml.py for old&target version of original lang file
1. diff.py
1. patch.py
1. (translate strings in the yaml file, including strings updated from the source, which are turned into nulls)
1. (optional) postprocess_ko_Kore.py
1. yaml_to_txt.py
