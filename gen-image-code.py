import os
import sys

def generate_html_code(directory_path, output_filename):
    with open(output_filename, 'w') as output_file:

        # write the first row
        output_file.write('<div class="row">\n')

        visible_file_count = 0

        # Loop through each file in the directory
        for filename in os.listdir(directory_path):

            # Check if the filename starts with a dot (hidden file)
            if not filename.startswith('.'):
                file_path = os.path.join(directory_path, filename)

                # Check if the path is a file (not a directory)
                if os.path.isfile(file_path):
                    visible_file_count += 1

                    # Generate the HTML code for each file
                    html_code = f'''
                    <div class="col-md-2">
                        <a class="fancybox" rel="group" href="{file_path}">
                            <div class="img-wrap">
                                <div class="overlay">
                                    <i class="fa fa-search"></i>
                                </div>
                                <img src="{file_path}" alt=""/>
                            </div>
                        </a>
                    </div>\n'''

                    # Write the HTML code to the output file
                    output_file.write(html_code)

                    # Add a new row every 6 items
                    if visible_file_count % 6 == 0:
                        output_file.write('</div>\n<div class="row">\n')

        #write the last row
        output_file.write('</div>\n')


if __name__ == "__main__":
    # Check if command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python gen-image-code.py <input_directory_path> <output_filename>")
        sys.exit(1)

    # Get input directory path and output filename from command line arguments
    input_directory_path = sys.argv[1]
    output_filename = sys.argv[2]

    generate_html_code(input_directory_path, output_filename)

