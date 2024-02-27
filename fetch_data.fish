set url "https://api.github.com/search/repositories?q=machine+learning+framework&sort=updated&per_page=100&page="

for page in 1 2 3 4 5;
    echo $page
    wget $url$page --output-document data/results-$page.json
end