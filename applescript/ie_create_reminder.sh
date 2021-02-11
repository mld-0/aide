#	Run Applescript as text from bash:
#	VIM SETTINGS: {{{3
#	VIM: let g:mldvp_filecmd_open_tagbar=0 g:mldvp_filecmd_NavHeadings="" g:mldvp_filecmd_NavSubHeadings="" g:mldvp_filecmd_NavDTS=0 g:mldvp_filecmd_vimgpgSave_gotoRecent=0
#	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#	vim: set foldlevel=2 foldcolumn=3: 
#	}}}1
#!/bin/bash

new_reminder_list_options=( "Pantheon" )

new_reminder_title="$1"
new_reminder_delta_min="$2"
new_reminder_list_id="$3"

#	Argument Default Values: "<TEST-ITEM>", "40", "0"
#	{{{3
new_reminder_title_default="<TEST-ITEM>";
if [[ -z "$new_reminder_title" ]]; then new_reminder_title="$new_reminder_title_default"; fi
new_reminder_delta_min_default="40";
if [[ -z "$new_reminder_delta_min" ]]; then new_reminder_delta_min="$new_reminder_delta_min_default"; fi
new_reminder_list_id_default="0"
if [[ -z "$new_reminder_list_id" ]]; then new_reminder_list_id="$new_reminder_list_id_default"; fi
#	}}}1

new_reminder_list="${new_reminder_list_options[@]:$new_reminder_list_id:1}"

osascript << EOF
tell application "Reminders"
	set reminder_list to "$new_reminder_list"
	set reminder_title to "$new_reminder_title"
	set reminder_delta_mins to $new_reminder_delta_min 

	-- Get Date and Time specified number of minutes from now as reminder_datetime
	set reminder_datetime to (current date) + (reminder_delta_mins * minutes)
	
	# Select the relevant list in Reminders.app
	set myList to list reminder_list
	
	tell myList
		# Create the reminder
		set newReminder to make new reminder
		set name of newReminder to reminder_title
		set remind me date of newReminder to reminder_datetime
	end tell
end tell
EOF


