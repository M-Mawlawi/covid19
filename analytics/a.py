with open(local_file, 'wb') as file:
    file.write(data.content)

with open(local_file) as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        row['Name'] = row.pop('ï»¿Name')
        key = row['Name']
        dataset[key] = row











    {%for a in flag%}
      {% for vkey,vval in val.items %}
      {%if a.name == val.Name%}
      {%if vval == none%}
      <td><img src="{{a.flag}}" height="50" width="70"></td>
      {%else%}
      <td>{{vval}}</td>
      {%endif%}
      {%endif%}
      {% endfor %}
      {%endfor%}