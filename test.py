import geocoder # pip install geocoder
g = geocoder.bing('Delhi, Ojaspranic Yoga yoga centre', key='AkM1C1tjs3zYcRsDCvrigXhmIKcy81N5o7J3VY8-paTqSKuQQSnMiIWAe3UN0u22')
results = g.json
print(results['lat'], results['lng'])