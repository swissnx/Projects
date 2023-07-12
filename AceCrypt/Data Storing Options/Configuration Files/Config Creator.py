
import os
import yaml
import json
from configparser import ConfigParser
import xml.etree.ElementTree as ET
from dotenv import load_dotenv, dotenv_values


class INI:
    def __init__(self):
        self.__config = ConfigParser()

    def __create_section(self, section: str):
        self.__config.add_section(section)

    def __create_key(self, section: str, key_name: str, key_value: str):
        self.__config.set(section, key_name, key_value)

    def __create_file(self, num_sections: int, sections: list):
        for i in range(num_sections):
            section = sections[i]['section_name']
            self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        with open('config.ini', 'w') as f:
            self.__config.write(f)
    
    def create_file(self, num_sections: int, sections: list):
        return self.__create_file(num_sections, sections)

    def __update_file(self, file_name: str, num_sections: int, sections: list):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        self.__config.read(file_name)
        current_contents = ''
        with open(file_name, 'r') as f:
            current_contents = f.read()

        for i in range(num_sections):
            section = sections[i]['section_name']
            if not self.__config.has_section(section):
                self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        with open(file_name, 'w') as f:
            self.__config.write(f)
        
        return current_contents
    
    def update_file(self, file_name: str, num_sections: int, sections: list):
        return self.__update_file(file_name, num_sections, sections)

    def __retrieve_key(self, file_name: str, section: str, key_name: str):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        self.__config.read(file_name)
        if not self.__config.has_section(section):
            return f"{section} does not exist."

        if self.__config.has_option(section, key_name):
            return self.__config.get(section, key_name)
        else:
            return f"{key_name} not found."
    
    def retrieve_key(self,file_name: str, section: str, key_name: str):
        return self.__retrieve_key(file_name, section, key_name)


class YAML:
    def __init__(self):
        self.__config = {}

    def __create_section(self, section: str):
        self.__config[section] = {}

    def __create_key(self, section: str, key_name: str, key_value: str):
        self.__config[section][key_name] = key_value

    def __create_file(self, num_sections: int, sections: list):
        for i in range(num_sections):
            section = sections[i]['section_name']
            self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        with open('config.yaml', 'w') as f:
            yaml.dump(self.__config, f)

    def create_file(self, num_sections: int, sections: list):
        return self.__create_file(num_sections, sections)

    def __update_file(self, file_name: str, num_sections: int, sections: list):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        with open(file_name, 'r') as f:
            self.__config = yaml.safe_load(f)

        current_contents = ''
        with open(file_name, 'r') as f:
            current_contents = f.read()

        for i in range(num_sections):
            section = sections[i]['section_name']
            if section not in self.__config:
                self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        with open(file_name, 'w') as f:
            yaml.dump(self.__config, f)
        
        return current_contents

    def update_file(self, file_name: str, num_sections: int, sections: list):
        return self.__update_file(file_name,num_sections , sections)

    def __retrieve_key(self, file_name: str, section: str, key_name: str):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        with open(file_name, 'r') as f:
            self.__config = yaml.safe_load(f)

        if section not in self.__config:
            return f"{section} does not exist."

        if key_name in self.__config[section]:
            return self.__config[section][key_name]
        else:
            return f"{key_name} not found."

    def retrieve_key(self, file_name: str, section: str, key_name: str):
        return self.__retrieve_key(file_name, section, key_name)


class JSON:
    def __init__(self):
        self.__config = {}

    def __create_section(self, section: str):
        self.__config[section] = {}

    def __create_key(self, section: str, key_name: str, key_value: str):
        self.__config[section][key_name] = key_value

    def __create_file(self, num_sections: int, sections: list):
        for i in range(num_sections):
            section = sections[i]['section_name']
            self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        with open('config.json', 'w') as f:
            json.dump(self.__config, f, indent=4)

    def create_file(self, num_sections: int, sections: list):
        return self.__create_file(num_sections, sections)

    def __update_file(self, file_name: str, num_sections: int, sections: list):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        with open(file_name, 'r') as f:
            self.__config = json.load(f)

        current_contents = ''
        with open(file_name, 'r') as f:
            current_contents = f.read()

        for i in range(num_sections):
            section = sections[i]['section_name']
            if section not in self.__config:
                self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        with open(file_name, 'w') as f:
            json.dump(self.__config, f, indent=4)
        
        return current_contents

    def update_file(self, file_name: str, num_sections: int, sections: list):
        return self.__update_file(file_name, num_sections, sections)

    def __retrieve_key(self, file_name: str, section: str, key_name: str):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        with open(file_name, 'r') as f:
            self.__config = json.load(f)

        if section not in self.__config:
            return f"{section} does not exist."

        if key_name in self.__config[section]:
            return self.__config[section][key_name]
        else:
            return f"{key_name} not found."

    def retrieve_key(self,file_name: str, section: str, key_name: str):
        return self.__retrieve_key(file_name, section, key_name)


class XML:
    def __init__(self):
        self.__config = ET.Element('config')

    def __create_section(self, section: str):
        ET.SubElement(self.__config, section)

    def __create_key(self, section: str, key_name: str, key_value: str):
        section_element = self.__config.find(section)
        if section_element is not None:
            key_element = ET.SubElement(section_element, key_name)
            key_element.text = key_value

    def __create_file(self, num_sections: int, sections: list):
        for i in range(num_sections):
            section = sections[i]['section_name']
            self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)

        tree = ET.ElementTree(self.__config)
        tree.write('config.xml')

    def create_file(self, num_sections: int, sections: list):
        return self.__create_file(num_sections, sections)

    def __update_file(self, file_name: str, num_sections: int, sections: list):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        tree = ET.parse(file_name)
        self.__config = tree.getroot()

        current_contents = ''
        with open(file_name, 'r') as f:
            current_contents = f.read()

        for i in range(num_sections):
            section = sections[i]['section_name']
            if self.__config.find(section) is None:
                self.__create_section(section)
            num_keys = sections[i]['num_keys']
            for j in range(num_keys):
                key_name = sections[i]['keys'][j]['key_name']
                key_value = sections[i]['keys'][j]['key_value']
                self.__create_key(section, key_name, key_value)
        tree.write(file_name)
        
        return current_contents

    def update_file(self, file_name: str, num_sections: int, sections: list):
        return self.__update_file(file_name, num_sections, sections)

    def __retrieve_key(self, file_name: str, section: str, key_name: str):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        tree = ET.parse(file_name)
        self.__config = tree.getroot()

        section_element = self.__config.find(section)
        if section_element is None:
            return f"{section} does not exist."

        key_element = section_element.find(key_name)
        if key_element is not None:
            return key_element.text
        else:
            return f"{key_name} not found."

    def retrieve_key(self, file_name: str, section: str, key_name: str):
        return self.__retrieve_key(file_name, section, key_name)


class ENV:
    def __init__(self):
        self.__config = {}

    def __create_key(self, key_name: str, key_value: str):
        self.__config[key_name] = key_value

    def __create_file(self, num_keys: int, keys: list):
        for j in range(num_keys):
            key_name = keys[j]['key_name']
            key_value = keys[j]['key_value']
            self.__create_key(key_name, key_value)

        with open('.env', 'w') as f:
            for key in self.__config:
                f.write(f"{key}={self.__config[key]}\n")

    def create_file(self, num_keys: int, keys: list):
        return self.__create_file(num_keys, keys)

    def __update_file(self, file_name: str, num_keys: int, keys: list):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        self.__config = dotenv_values(file_name)
        current_contents = ''
        for key in self.__config:
            current_contents += f"{key}={self.__config[key]}\n"

        for j in range(num_keys):
            key_name = keys[j]['key_name']
            key_value = keys[j]['key_value']
            self.__create_key(key_name, key_value)

        with open(file_name, 'w') as f:
            for key in self.__config:
                f.write(f"{key}={self.__config[key]}\n")
        
        return current_contents

    def update_file(self, file_name: str, num_keys: int, keys: list):
        return self.__update_file(file_name, num_keys, keys)

    def __retrieve_key(self, file_name: str, key_name:str):
        if not os.path.exists(file_name):
            return f"{file_name} does not exist."

        self.__config = dotenv_values(file_name)
        if key_name in self.__config:
            return f"{key_name}={self.__config[key_name]}"
        else:
            return f"{key_name} not found."

    def retrieve_key(self, file_name: str, key_name: str):
        return self.__retrieve_key(file_name, key_name)


class Config:
    def __init__(self):
        self.ini_configurator = INI()
        self.yaml_configurator = YAML()
        self.json_configurator = JSON()
        self.xml_configurator = XML()
        self.dot_env_var = ENV()

    def __run(self):
        while True:
            print("\n1. Create Config/Env_Var files\n2. Update the file\n3. Retrieve Key\n0. Exit")
            choice = input("\nAction: ")

            if choice == "1":
                print("\nFile Type:\n1. ini\n2. yaml\n3. json\n4. xml\n5. env_var")
                config_pick = input("\nConfig: ")

                if config_pick == '1':
                    num_sections=int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    self.ini_configurator.create_file(num_sections=num_sections, sections=sections )
                    
                elif config_pick == '2':
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    self.yaml_configurator.create_file(num_sections=num_sections, sections=sections )
                    
                elif config_pick == '3':
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    self.json_configurator.create_file(num_sections=num_sections ,sections=sections )
                    
                elif config_pick == '4':
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    self.xml_configurator.create_file(num_sections=num_sections ,sections=sections )
                    
                elif config_pick == '5':
                    num_keys = int(input("\nNumber of Keys: "))
                    keys = []
                    for j in range(num_keys):
                        key = {}
                        key['key_name'] = input(f"\nName of Key #{j+1}: ")
                        key['key_value'] = input("Key Value: ")
                        keys.append(key)
                        
                    self.dot_env_var.create_file(num_keys=num_keys ,keys=keys )
                    
                print("\nFile Created!")

            elif choice == "2":
                print("\nFile Type:\n1. ini\n2. yaml\n3. json\n4. xml\n5. env_var")
                config_pick = input("\nConfig: ")

                if config_pick == '1':
                    file_path = input("\nFile Path: ")
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    print("\nCurrent contents of the file:")
                    print(self.ini_configurator.update_file(file_path,num_sections=num_sections ,sections=sections))
                    
                elif config_pick == '2':
                    file_path = input("\nFile Path: ")
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    print("\nCurrent contents of the file:")
                    print(self.yaml_configurator.update_file(file_path,num_sections=num_sections ,sections=sections))
                    
                elif config_pick == '3':
                    file_path = input("\nFile Path: ")
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    print("\nCurrent contents of the file:")
                    print(self.json_configurator.update_file(file_path,num_sections=num_sections ,sections=sections))
                    
                elif config_pick == '4':
                    file_path = input("\nFile Path: ")
                    num_sections = int(input("\nNumber of Sections: "))
                    sections = []
                    for i in range(num_sections):
                        section = {}
                        section['section_name'] = input(f"\nName of Section #{i+1}: ")
                        section['num_keys'] = int(input("Number of Keys: "))
                        keys = []
                        for j in range(section['num_keys']):
                            key = {}
                            key['key_name'] = input(f"\nName of Key #{j+1}: ")
                            key['key_value'] = input("Key Value: ")
                            keys.append(key)
                        section['keys'] = keys
                        sections.append(section)
                        
                    print("\nCurrent contents of the file:")
                    print(self.xml_configurator.update_file(file_path,num_sections=num_sections ,sections=sections))
                    
                elif config_pick == '5':
                    file_path = input("\nFile Path: ")
                    num_keys = int(input("\nNumber of Keys: "))
                    keys = []
                    for j in range(num_keys):
                        key = {}
                        key['key_name'] = input(f"\nName of Key #{j+1}: ")
                        key['key_value'] = input("Key Value: ")
                        keys.append(key)
                        
                    print("\nCurrent contents of the file:")
                    print(self.dot_env_var.update_file(file_path,num_keys=num_keys ,keys=keys))
                    
                print("\nFile Updated!")

            elif choice == "3":
                print("\nWhich Config file:\n1. ini\n2. yaml\n3. json\n4. xml\n5. env_var")
                config_pick = input("\nConfig: ")
                if config_pick == '1':
                    file_path = input("\nFile Path: ")
                    section = input("\nSection Name: ")
                    key_name = input("Key Name: ")
                    print(self.ini_configurator.retrieve_key(file_path,section,key_name))
                    
                elif config_pick == '2':
                    file_path = input("\nFile Path: ")
                    section = input("\nSection Name: ")
                    key_name = input("Key Name: ")
                    print(self.yaml_configurator.retrieve_key(file_path,section,key_name))
                    
                elif config_pick == '3':
                    file_path = input("\nFile Path: ")
                    section = input("\nSection Name: ")
                    key_name = input("Key Name: ")
                    print(self.json_configurator.retrieve_key(file_path,section,key_name))
                    
                elif config_pick == '4':
                    file_path = input("\nFile Path: ")
                    section = input("\nSection Name: ")
                    key_name = input("Key Name: ")
                    print(self.xml_configurator.retrieve_key(file_path,section,key_name))
                    
                elif config_pick == '5':
                    file_path = input("\nFile Path: ")
                    key_name = input("\nKey Name: ")
                    print(self.dot_env_var.retrieve_key(file_path,key_name))

            elif choice == "0" or choice == "":
                break

    def run(self):
        try:
            self.__run()

        except ValueError as ve:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"


if __name__ == "__main__":
    config = Config()
    config.run()
