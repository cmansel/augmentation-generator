FROM python:3.7

WORKDIR /augmentation_generator

COPY ./requirements /augmentation_generator/requirements

RUN pip install -r requirements/dev.txt
RUN pip install -r requirements/prod.txt

COPY . /augmentation_generator

CMD [ "./run_with_tests.sh" , "1", "5", "29" ]