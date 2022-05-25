FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/wf-base:fbe8-main
# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#Install pandas
RUN pip install pandas
# Install cialign using pip
RUN pip3 install cialign

RUN mkdir /root/cia_output

COPY wf /root/wf

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN  sed -i 's/latch/wf/g' flytekit.config
RUN  sed -i 's/latch/wf/g' flytekit.config
RUN python3 -m pip install --upgrade latch
WORKDIR /root
#ENV LATCH_AUTHENTICATION_ENDPOINT https://nucleus.latch.bio
