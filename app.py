# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:17:19 2020

@author: rejid4996
"""

# importing packages
import streamlit as st
import os
#import time
import fitz
#import shutil
import numpy as np
import pandas as pd
#from keras.models import load_model
#from keras.preprocessing import image

# export function to push the data to concerned folder

    
def main():
    from PIL import Image
    logo = Image.open('ArcadisLogo.jpg')
    logo = logo.resize((300,90))
    
    wallpaper = Image.open('contamination_site.jpg')
    wallpaper = wallpaper.resize((700,350))
    
    st.sidebar.image(logo)
    st.image(wallpaper)
    st.sidebar.title("AI for Site Summaries")
    st.sidebar.subheader("Image Extraction ")
    
    st.info("Extraction of Images for Site Summary reports")
    
    input_path = st.sidebar.text_input("path to the historical documents", "")
    output_path = st.sidebar.text_input("output path to the results", "")
    site_name = st.sidebar.text_input("Enter the Site name", "")
    
    if site_name:
        os.chdir(output_path)
        #site_name = 'Area 5' # user selection
        site_folder = output_path + '\\' + site_name
        contamination_plume = site_folder + '\\' + '01_contamination plume'
        conceptual_sitemodel = site_folder + '\\' + '02_conceptual sitemodel'
        remediation_designs = site_folder + '\\' + '03_remediation designs'
        conceptual_remedial_design = site_folder + '\\' + '04_conceptual remedial design'
        land_use = site_folder + '\\' + '05_land use'
        hydraulic_capture = site_folder + '\\' + '06_hydraulic capture'
        exposure_pathways = site_folder + '\\' + '07_exposure pathways'
        groundwater_sampling = site_folder + '\\' + '08_groundwater sampling'
        proposed_wells = site_folder + '\\' + '09_proposed wells'
        boring_locations = site_folder + '\\' + '10_boring locations'
        well_locations = site_folder + '\\' + '11_well locations'
        site_map = site_folder + '\\' + '12_site map'
        groundwater_flowMaps = site_folder + '\\' + '13_GW flowmap'
        trend_data = site_folder + '\\' + '14_trend data'
        cross_sections = site_folder + '\\' + '15_cross sections'
        potentiometric_maps = site_folder + '\\' + '16_potentiometric_maps'
        
    
        miscellaneous = site_folder + '\\' + '17_miscellaneous'
        filtered_images = site_folder + '\\' + '18_recycle bin'
        
        directories = [contamination_plume, conceptual_sitemodel, remediation_designs, conceptual_remedial_design, land_use, hydraulic_capture, exposure_pathways, groundwater_sampling, proposed_wells, boring_locations, well_locations, site_map, groundwater_flowMaps, trend_data, cross_sections, potentiometric_maps, miscellaneous]
    
        # To create sitename folder only if it doesn't exist
        if not os.path.exists(site_name):
            os.mkdir(site_name)
        
        os.chdir(site_folder) # To set working directory 
        
        # Creation of directories
        folder_names = ['01_contamination plume', '02_conceptual sitemodel', '03_remediation designs', '04_conceptual remedial design', '05_land use', '06_hydraulic capture', '07_exposure pathways', '08_groundwater sampling', '09_proposed wells', '10_boring locations', '11_well locations', '12_site map', '13_GW flowmap', '14_trend data', '15_cross sections', '16_potentiometric_maps','17_miscellaneous', '18_recycle bin']
           
        for names in folder_names:
            if not os.path.exists(names):
                os.makedirs(names)
        
        # identifiers
        plume_identifiers = ['plume', 'isoconcentration', 'iso-concentration', 'isosurface', 'iso-surface', 'extent', 'concentration map']
        site_map_identifiers = ['site location', 'site map', 'location map', 'site overview', 'site layout', 'site vicinity', 'site features', 'study area', 'site detail']
        potentiometric_identifiers = ['potentiometric', 'contour', 'groundwater elevation']
        trend_identifiers = ['trend', 'concentration graphs', 'performance plot', 'performance model', 'projected concentrations','time series', 'timeframe', 'time required']
        cross_sections_identifiers = ['cross section', 'cross-section', "a-a'", "b-b'", 'geologic profile', "c-c'", "d-d'", ]
        sampling_identifiers = ['groundwater sample', 'concentration', 'detections', 'detected', 'groundwater sampling', 'analytical'] 
        well_location_identifiers = ['well location', 'monitoring well location', 'location of monitoring wells', 'extraction well location', 'monitor well', 'groundwater sample location', 'groundwater sampling location', 'location of extraction wells', 'well network'] 
        remediation_design_identifiers = ['remediation', 'treatment','system', 'injection', 'insitu', 'in-situ', 'isco', 'manifold', 'trench', 'civil', 'piping', 'process', 'instrumentation diagram', 'p&id', 'pid', 'bioreactor', 'as-built', 'biosparg', 'sve','sparge', 'reactor', 'pump control', 'well box details', 'well head details', 'extraction', 'excavation', 'design', 'leachate collection','thermal treatment']
        exposure_pathway_identifiers = ['exposure pathway', 'exposure route', 'exposure mechanism', 'source-receptor', 'source-pathway', 'transport mechanism']
        conceptual_sitemodel_identifiers = ['conceptual site', 'site conceptual', 'csm', 'scm', 'conceptual model']
        conceptual_remedial_design_layouts_identifiers = ['conceptual remed', 'conceptual cross-section', 'proposed remediation infrastructure', 'alternative', 'selected remedy', 'conceptual target', 'feasibility']
        land_use_figures = ['land use', 'landuse restrictions', 'institutional controls', 'restricted areas', 'engineering controls', 'restriction', 'luc', 'ic']   
        hydraulic_capture_maps = ['capture zone', 'pump and treat', 'pump & treat']
        proposed_wells_identifiers = ['proposed location', 'proposed well', 'proposed monitoring well', 'proposed extraction well', 'proposed injection well']
        soil_boring_locations_identifiers = ['soil boring', 'soil sample', 'soil sampling', 'borehole', 'bore-hole', 'sample points', 'mg/kg', 'μg/kg', 'soil results', 'soil copcs', 'subsurface investigation', 'subsurface evaluation', 'soil detections', 'soil concentrations', 'detected in soil', 'soil investigation', 'soil vapor', 'soil gas', 'surface soil', 'sediment', 'ppmv', 'ppbv', 'soil-vapor', 'soil-Gas']
        
        def export(page_number, input, output):
            os.chdir(input)
            zoom = 2    # zoom factor
            mat = fitz.Matrix(zoom, zoom)
            pix = page_number.getPixmap(matrix = mat)
            os.chdir(output)
            pix.writePNG(str(page_n)[:-4] + ".png")
            os.chdir(input)
        
        # exception check
        Total_file_count = len(os.listdir(input_path)) # input files
        total_pagecount = 0 # to calculate page count
        pageexceptions = [] # to track the pages which are not working
        fileexceptions = [] # to track the file exceptions
        
        os.chdir(input_path)
        for i in os.listdir():
            
            print(i + " is in progress...................................")
            
            try:
                # loading the pdf file using fitz package
                doc = fitz.open(i)
                
                # storing the page count
                n = doc.pageCount
                
                total_pagecount+=n # appending page count
                
                # looping through the page number and extracting text
                for page in range(0,n):   
                    try:
                        page_n = doc.loadPage(page)
                        page_text = page_n.getText("text").lower()
                          
                        if any(word in page_text for word in ['figure', 'legend']): 
                            
                            # if all the words are matching, for extracting plume maps <---
                            if any(word in page_text for word in plume_identifiers):   
                                print("plume figures")
                                export(page_n, input = input_path, output = contamination_plume)
                                
                            # for extracting site maps <---
                            elif any(word in page_text for word in site_map_identifiers):
                                print("site maps")
                                export(page_n, input = input_path, output = site_map)
                            
                            # for extracting potentiometric maps <---
                            elif any(word in page_text for word in potentiometric_identifiers):
                                print("potentiometric maps")
                                export(page_n, input = input_path, output = potentiometric_maps)
                            
                            # for extracting trend maps <---
                            elif any(word in page_text for word in trend_identifiers):
                                print("trend maps")
                                export(page_n, input = input_path, output = trend_data)
                            
                            # for extracting cross section maps <---
                            elif any(word in page_text for word in cross_sections_identifiers):
                                print("cross section maps")
                                export(page_n, input = input_path, output = cross_sections)
                                
                            # for groundwater sampling figures <---
                            elif any(word in page_text for word in sampling_identifiers):
                                print("groundwater sampling figures")
                                export(page_n, input = input_path, output = groundwater_sampling)
                            
                            # for well location  figures <---
                            elif any(word in page_text for word in well_location_identifiers):
                                print("well location figures")
                                export(page_n, input = input_path, output = well_locations)
                            
                            # for remediation figures <---
                            elif any(word in page_text for word in remediation_design_identifiers):
                                print("remediation figures")
                                export(page_n, input = input_path, output = remediation_designs)
                    
                            # for exposure pathway figures <---
                            elif any(word in page_text for word in exposure_pathway_identifiers):
                                print("exposure pathway figures")
                                export(page_n, input = input_path, output = exposure_pathways)
                    
                            # for conceptual site model figures <---
                            elif any(word in page_text for word in conceptual_sitemodel_identifiers):
                                print("conceptual sitemodel figures")
                                export(page_n, input = input_path, output = conceptual_sitemodel)
                    
                            # for conceptual remedial design layouts identifiers figures <---
                            elif any(word in page_text for word in conceptual_remedial_design_layouts_identifiers):
                                print("conceptual remedial design figures")
                                export(page_n, input = input_path, output = conceptual_remedial_design)
                            
                            # for land use figures figures <---
                            elif any(word in page_text for word in land_use_figures):
                                print("land use figures")
                                export(page_n, input = input_path, output = land_use)
                            
                            # for hydraulic capture maps figures <---
                            elif any(word in page_text for word in hydraulic_capture_maps):
                                print("hydraulic capture maps figures")
                                export(page_n, input = input_path, output = hydraulic_capture)
                            
                            # for proposed wells identifiers figures <---
                            elif any(word in page_text for word in proposed_wells_identifiers):
                                print("proposed wells figures")
                                export(page_n, input = input_path, output = proposed_wells)
                            
                            # for soil boring locations figures <---
                            elif any(word in page_text for word in soil_boring_locations_identifiers):
                                print("soil boring locations figures")
                                export(page_n, input = input_path, output = boring_locations)
                                
                    except:
                        print("this page is not running")
                        pageexceptions.append(str(page_n)[:-4])
                        try:
                            export(page_n, input = input_path, output = miscellaneous)
                            os.chdir(input_path) 
                        except:
                            print("except condition without pushing the image")
                    
                    if page_text == "":
                        print("chance of figure")
                        export(page_n, input = input_path, output = miscellaneous)
                     
            except:
                print(i + " file is not working")
                fileexceptions.append(str(page_n)[:-4])
    
if __name__ == "__main__":
    main()



