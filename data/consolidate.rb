require 'csv'

csv_data = CSV.read('SIEVO JUNCTION Spend data copy.csv').drop(1)


res = Hash.new {|h,k| h[k] = {}}
csv_data.each do |(key, product_name, spend_eur, quantity, uom, vendor_id, vendor_name, vendor_city, vendor_country, category1, category2 )|
  res[key]['product_name'] = product_name
  res[key]['spend_eur'] = res[key]['spend_eur'].to_f + spend_eur.to_f
case uom
  when 'KG'
    res[key]['quantity'] = res[key]['quantity'].to_f + quantity.to_f
  when 'G'
    res[key]['quantity'] = res[key]['quantity'].to_f + (quantity.to_f/1000)
  when 'ST'
    res[key]['quantity'] = res[key]['quantity'].to_f + (quantity.to_f * 6.350293)
end
res[key]['vendor_id'] = vendor_id if res[key]['vendor_id'].nil?
res[key]['vendor_id'] = [res[key]['vendor_id'], vendor_id].join(', ') if !res[key]['vendor_id'].nil? && !res[key]['vendor_id'].include?(vendor_id)

res[key]['vendor_name'] = vendor_name if res[key]['vendor_name'].nil?
res[key]['vendor_name'] = [res[key]['vendor_name'], vendor_name].join(', ') if !res[key]['vendor_name'].nil? && !res[key]['vendor_name'].include?(vendor_name)

res[key]['vendor_city'] = vendor_city if res[key]['vendor_city'].nil?
res[key]['vendor_city'] = [res[key]['vendor_city'], vendor_city].join(', ') if !res[key]['vendor_city'].nil? && !res[key]['vendor_city'].include?(vendor_city)

res[key]['vendor_country'] = vendor_country if res[key]['vendor_country'].nil?
res[key]['vendor_country'] = [res[key]['vendor_country'], vendor_country].join(', ') if !res[key]['vendor_country'].nil? && !res[key]['vendor_country'].include?(vendor_country)

res[key]['category1'] = category1
res[key]['category2'] = category2
end

CSV.open("spend_data.csv", "wb") do |csv|
  # sort res hash by keys, map to have array of values and add to csv
  csv << ['ProductName','SpendEUR','Quantity','VendorId','VendorName','VendorCity','VendorCountry','CategoryL1','CategoryL2']
  res.each do |re|
    csv << re[1].values
  end
end
