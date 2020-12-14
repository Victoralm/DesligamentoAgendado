# Desligamento Agendado

Script Python contendo uma GUI [ttk](https://docs.python.org/3/library/tkinter.ttk.html) para agendar o desligamento do PC em ambientes Windows e Linux.

## Como usar

### Windows 10 64b

- Instalar o [Python](https://www.python.org/downloads/)
- Certificar-se que este esteja nas variáveis de ambiente (seja do sistema ou do usuário)
- No terminal, executar:
  - `pip install pillow`
- Executar o script
- Opcionalmente, pode-se criar um atalho na Área de Trabalho para o script

### Ubuntu 20.04 64b

- No Terminal, executar:
  - `sudo apt install python3`
  - `sudo apt install python3-pip`
  - `sudo apt install python3-pil.imagetk`
- Executar o script
- Opcionalmente, pode-se criar um atalho (*.desktop) na Área de Trabalho para
  o script, em `~/.local/share/applications`

#### `DeslAutom.desktop` template

```bash
#!/usr/bin/env python3
[Desktop Entry]
Name=Desligamento Agendado
Comment=Python ttk GUI para agendamento do desligamento do PC
Icon=<inserir_caminho_completo>/powerDown01.png
Exec=python3 <inserir_caminho_completo>/AlmsDesligamentoPC.py
Path=<inserir_caminho_completo>/
Terminal=false
Type=Application
Categories=Utility;Application;
```
