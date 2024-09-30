spiders=("ita-undergraduate" "usp-undergraduate" "ufsc-undergraduate" "ufmg-undergraduate" "ufcg-undergraduate")

for spider in "${spiders[@]}"; do
    echo "Iniciando spider $spider..."
    
    scrapy crawl "$spider"
    
    if [ $? -eq 0 ]; then
        echo "Spider $spider finalizado com sucesso."
    else
        echo "Spider $spider falhou."
        exit 1
    fi
done
