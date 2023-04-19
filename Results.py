tile_clicks = {1: 0, 2: 0, 3: 0, 4: 0}

with open('pianotiles_data.txt', 'r') as f:
    for line in f:
        if 'Clicked 1st Tile' in line:
            tile_clicks[1] += 1
        elif 'Clicked 2nd Tile' in line:
            tile_clicks[2] += 1
        elif 'Clicked 3rd Tile' in line:
            tile_clicks[3] += 1
        elif 'Clicked 4th Tile' in line:
            tile_clicks[4] += 1

total_clicks = sum(tile_clicks.values())
for tile, clicks in tile_clicks.items():
    percentage = (clicks / total_clicks) * 100
    print(f'Tile {tile}: {clicks} clicks making it {percentage:.2f}% of the total clicks')
