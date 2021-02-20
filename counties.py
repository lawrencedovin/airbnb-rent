import itertools

montgomery_county = ['Rockville', 'Bethesda', 'Gaithersburg', 'Germantown', 'Olney',
            'Potomac', 'Takoma Park', 'Monthgomery Village', 'Wheaton', 'Clarksburg',
            'White Oak', 'Kensington', 'Burtonsville', 'North Potomac', 'North Bethesda',
            'Poolesville', 'Aspen Hill', 'Boyds', 'Darnestown', 'Damascus',
            'Brookeville', 'Colesville', 'Garrett Park', 'Laytonsville', 'Chevy Chase',
            'Washington Grove', 'Cabin John', 'Glen Echo', 'Fairland', 'Barnesville',
            'Leisure World', 'Cloverly', 'Dickerson', 'Kemp Mill', 'Travilah',
            'Chevy Chase View', 'Ashton-Sandy Spring', 'Friendship Village', 'North Kensington',
            'Kensingston', 'South Kensington', 'Redland', 'Brookmont', 'Somerset',
            'Silver Spring']

anne_arrundel_county = ['Annapolis', 'Crofton', 'Severn', 'Fort Meade', 'Deale', 
            'Galesville', 'Parole', 'Arden-on-the-Servern', 'Highland Beach', 'Glen Burnie',
            'Severna Park', 'Arnold', 'Crownsville', 'Cape Saint Claire', 'Riviera Beach',
            'Maryland City', 'Selby-on-the-Bay', 'Pasadena', 'Millersville', 'Gambrills',
            'Brooklyn Park', 'Mayo', 'Riva', 'Russett', 'Herald Harbor',
            'Odenton', 'Edgewater', 'Linthicum Heights', 'Shady Side', 'Ferndale',
            'Lake Shore', 'Londontowne', 'Friendship']

prince_george_county = ['Bowie', 'Clinton', 'Fort Washington', 'Capitol Heights', 'District Heights',
            'Mount Rainier', 'Berwyn Height', 'Brentwood', 'Edmonston', 'Seabrook',
            'North Brentwood', 'Colmar Manor', 'Westphalia', 'Upper Marlboro', 'Largo',
            'Oxon Hill', 'Temple Hills', 'Bladensburg', 'University Park', 'Glenarden',
            'Mitchellville', 'Chillum', 'Hillcrest Heights', 'Marlow Heights', 'Forest Heights',
            'Queenland', 'Laurel', 'College Park', 'Cheverly', 'Beltsville',
            'Riverdale Park', 'Accokeek', 'Adelphi', 'Camp Spring', 'Fairmont Heights',
            'Woodmore', 'Aquasco', 'Morningside', 'Glassmanor', 'Hyattsville',
            'Greenbelt', 'Lanham', 'Brandywine', 'New Carrollton', 'Forestville',
            'Langley Park', 'Glenn Dale', 'Landover Hills', 'Kettering', 'Cottage City',
            'Walker Mill']

frederick_county = ['Frederick', 'New Market', 'Emmitsburg', 'Jefferson', 'Adamstown',
            'Sabillasville', 'Urbana', 'Walkersville', 'Monrovia', 'Buckeystown',
            'Burkittsville', 'Rosemont', 'Thurmont', 'Ballenger Creek', 'Clover Hill',
            'Woodsboro', 'Libertytown', 'Green Valley', 'Middletown', 'Brunswick',
            'Myersville', 'Point of Rocks', 'Braddock Heights', 'Discovery-Spring Garden']

cities = list(itertools.chain(montgomery_county, anne_arrundel_county, prince_george_county, frederick_county))

