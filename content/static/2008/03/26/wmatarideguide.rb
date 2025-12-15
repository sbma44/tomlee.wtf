require 'rubygems'
require 'mechanize'
require 'timedcache'
require 'time'
require 'chronic'

class WMATARideGuide

  def initialize	
		@agent = WWW::Mechanize.new		
	end  
  
  def get_next_time(origin, destination, travel_mode = :rail)
    	# retrieve the page
  		page = @agent.get('http://www.wmata.com/tripplanner_d/TripPlanner_Form_Solo.cfm')

  		# fill out and submit the form
  		form = page.form('LocateCall')
  		
  		# make sure the time is properly set
  		form.Time = Time.now.strftime('%I:%M')
  		form.AMPM = Time.now.strftime('%p')
  		form.ArrDep = 'D'
  		form.dateMonth = Time.now.strftime('%m')
  		form.dateDay = Time.now.strftime('%d')
  		form.dateYear = Time.now.strftime('%Y')
  		
  		# set where we're coming from, where we're going
  		form.StreetAddressFrom = origin
  		form.StreetAddressTo = destination
  		
  		# specify bus or rail
  		form.Mode = ((travel_mode==:rail) ? 'R' : 'B');

      # submit
  		result = @agent.submit(form)
  		
  		#check to see if both destinations were specific enough
  		ambiguous_message = (result/('.content > p > b'))
  		if(ambiguous_message.length>0)
  		  if(ambiguous_message.first.inner_html.downcase.include? 'not found')
  		    return :ambiguous
  		  end
		  end

  		# grab the contents of the first cell in the third row of the table in div#itinDiv1
  		result_cells = (result/("#itinDiv1 table tr:nth(3) td"))

  		if result_cells.length>0 
  			result_cell_html = result_cells.first.inner_html

  			# match the time string
  			match = result_cell_html.scan(/at\s(\d{1,2}:\d{2}\s*(am|pm))/i)

  			# if we found a match...
  			if match.length>0
  				t = Chronic.parse(match[0][0])
  				return t
  			end	
  		end

  		return :not_found
  end

end
