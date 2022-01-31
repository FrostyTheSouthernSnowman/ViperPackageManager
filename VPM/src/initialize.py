import typer


def initialize_proj():
    with open("viper.yml", "w+") as f:
        f.write("""scripts:
    - echo \"no scripts set in viper.yml\n
requirement:
    - pip""")
