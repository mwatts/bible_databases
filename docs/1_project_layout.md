## Project Structure

### Formats Folder

The `formats` folder is the main source of biblical texts in various formats converted by our script from consistent accurate sources. It houses the converted data in multiple formats such as MySQL, CSV, JSON, YAML, TXT, and MD, making it accessible for different use cases and integrations.

### Scripts Folder

The `scripts` folder contains essential Python scripts designed to manage and extend the functionality of the Scrollmapper Bible databases. These scripts facilitate the creation, conversion, and management of Bible translations and related data.

### Sources Folder

The `sources` folder contains the source data files for each Bible translation, organized by language and translation. For example, English translations are stored under the `en` subfolder, with each translation in its own directory.

Each translation directory includes the cleaned source JSON used to generate the files in `formats`, a README with translation details, and when available, a corresponding OSIS JSON file. OSIS, the Open Scripture Information Standard, is an XML-based scripture markup standard maintained by CrossWire: https://crosswire.org/osis/

The OSIS JSON files are included for developer convenience and preserve more of the original source markup. They are not currently expanded into every generated format in order to keep the repository smaller and avoid format-specific issues caused by complex markup and special characters. The OSIS JSON structure corresponds to the matching cleaned JSON output, allowing developers to compare or use both versions as needed.
