
RED='\033[1;31m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RESET='\033[0m'

clear
echo -e "${RED}"
echo "        (\_/)      " 
echo "        (•_•)      " 
echo "        />❤️       " 
echo -e "${YELLOW}     << LOVERTY >>"
echo -e "${BLUE}   by mohamed ilkhadry"
echo -e "${RESET}"

sleep 2

echo -e "${CYAN}[+] Checking & Installing Requirements...${RESET}"
pkg install -y python python2 python3 pip > /dev/null 2>&1
pip install requests rich bs4 > /dev/null 2>&1
echo -e "${GREEN}[✓] Requirements Installed Successfully!${RESET}"

sleep 1
echo -e "${CYAN}[+] Launching LOVERTY Tool...${RESET}"
sleep 1

python3 LVF.py
