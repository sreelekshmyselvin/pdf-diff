#-*- coding: utf-8 -*-
"""
Created on 07/02/20 12:17 PM
@author : Sreelekshmy Selvin

"""
import differenceanalyser as analyser
import config

def processPDF(filename1,filename2):
	styles = config.STYLES
	style = styles.split(',')
	result_width = config.WIDTH
	changes = analyser.compute_changes(filename1, filename2)
	img = analyser.render_changes(changes, style, result_width)
	img.save("comparison11.png")
	finalstatus = 'File comparison successful'
	return finalstatus


if __name__ == '__main__':
	filename1 = 'draft.pdf'
	filename2 = 'final.pdf'
	processPDF(filename1,filename2)

