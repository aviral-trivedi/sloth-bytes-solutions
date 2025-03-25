#Remove the Computer Virus
def remove_virus(virus_text: str):
    """
    Removes the virus files from a set of files

    Args:
        virus_text (str) : the string of text to remove virusus from
    
    Returns:

    """

    excluded_names = ("antivirus", "notvirus")

    mix_files = virus_text[10:].split()
    clean_files = []
    
    
    for file_name in mix_files:
        item = file_name.partition(".")[0]
        if not item.endswith("virus") and not item.endswith("malware")  or item in excluded_names:
            clean_files.append(file_name)
    
    checked_data = f"PC Files: {' '.join(clean_files)}"

    print(checked_data)



remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
remove_virus("PC Files: notvirus.exe, funnycat.gif")

output = "PC Files: spotifysetup.exe, dog.jpg"
output = "PC Files: antivirus.exe, cat.pdf"
output = "PC Files: notvirus.exe, funnycat.gif"